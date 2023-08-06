#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from pg_metadata._System import SEP
from pg_metadata.ACL     import ACL
from pg_metadata.Owner   import Owner
from pg_metadata.Comment import Comment

class Table():
    def __init__(self, row={}, ddl_style=""):
        assert row is not None
        assert isinstance(row, dict)
        assert len(row.keys()) > 0

        self.Type = "TABLE"

        self.Oid = row.get('oid')
        assert self.Oid is not None and self.Oid > 0

        self.HasOids = row.get('has_oids') or ''
        self.HasOids = self.HasOids.strip()
        assert len(self.HasOids) > 0

        self.Schema = row.get('schema') or ''
        self.Schema = self.Schema.strip()
        assert len(self.Schema) > 0

        self.Name = row.get('name') or ''
        self.Name = self.Name.strip()
        assert len(self.Name) > 0

        self.FullName = "%s.%s" % (self.Schema, self.Name)

        self.Inherits = row.get('parent_table') or ''
        self.Inherits = self.Inherits.strip()

        self.Inherits = row.get("parent_table")
        if self.Inherits is not None and self.Inherits != '':
            self.Inherits = self.Inherits.strip()
        else:
            self.Inherits = None

        self.PartKey = row.get("part_key")
        if self.PartKey is not None and self.PartKey != "":
            self.PartKey = self.PartKey.strip()
        else:
            self.PartKey = None

        self.PartBorder = row.get("part_border")

        self.Folder = "table"

        self.DDLStyle = ddl_style

        self.Owner = Owner(
            self.Type,
            self.FullName,
            row.get("owner"),
            self.DDLStyle
        )

        self.Comment = Comment(
            self.Type,
            self.FullName,
            row.get("comment"),
            self.DDLStyle
        )

        self.ACL = ACL(
            self.Type,
            self.FullName,
            self.Owner.Owner,
            row.get("relacl"),
            self.DDLStyle
        )

        self.Settings = row.get("reloptions")

        self.Columns     = []
        self.Constraints = []
        self.Indexes     = []
        self.Triggers    = []

    def __str__(self):
        return self.FullName

    def QueryRemove(self):
        return 'DROP TABLE IF EXISTS %s;' % (self.FullName)

    def QueryAdd(self, columns_inside=False):
        result = ""
        result += "CREATE TABLE %s()" % (self.FullName)
        result += SEP

        if self.PartKey is not None:
            result += "PARTITION BY %s" % (self.PartKey)
            result += SEP

        if self.Inherits is not None:
            if self.PartBorder is not None:
                result += "PARTITION OF %s" % (self.Inherits)
                result += SEP
            else:
                result += "INHERITS ( %s )" % (self.Inherits)
                result += SEP

        if self.PartBorder is not None:
            result += self.PartBorder
            result += SEP

        result += "WITH ("
        result += SEP
        result += self.QuerySettings()
        result += SEP
        result += ");"
        result += SEP

        return result

    def QuerySettings(self):
        r = []

        r.append("  OIDS=%s" % (str(self.HasOids).upper()))

        if self.Settings is not None:
            for sts in self.Settings:
                r.append("  %s" % (sts))

        return (",%s" % (SEP)).join(r)

    def QueryDDL(self):
        is_last_comma = len(self.Constraints) > 0

        result = ''
        result += self.QueryRemove()
        result += SEP
        result += SEP

        result += "CREATE TABLE %s(" % (self.FullName)
        result += SEP

        # Столбцы
        for col in self.Columns:
            result += col.QueryRaw(add_comma=is_last_comma, add_comment=True)
            result += SEP

        # Ограничения
        for i, cns in enumerate(self.Constraints):
            comma = "" if (i + 1 == len(self.Constraints)) else ","
            result += "  " + cns.QueryRaw() + comma
            result += SEP

        result += ")"
        result += SEP

        if self.PartKey is not None:
            result += "PARTITION BY %s" % (self.PartKey)
            result += SEP

        if self.Inherits is not None:
            if self.PartBorder is not None:
                result += "PARTITION OF %s" % (self.Inherits)
                result += SEP
            else:
                result += "INHERITS ( %s )" % (self.Inherits)
                result += SEP

        if self.PartBorder is not None:
            result += self.PartBorder
            result += SEP

        result += "WITH ("
        result += SEP
        result += self.QuerySettings()
        result += SEP
        result += ");"
        result += SEP
        result += SEP
        result += self.Owner.DDL_Create()
        result += SEP
        result += self.ACL.DDL_Create()
        result += SEP
        result += SEP

        if self.Comment.IsExists:
            result += self.Comment.DDL_Create()
            result += SEP
            result += SEP

        for col in self.Columns:
            cmt = col.QueryComment()
            if cmt is not None:
                result += col.QueryComment()
                result += SEP
        result += SEP

        for ind in sorted(self.Indexes, key=lambda x: x.FullName):
            result += ind.QueryAdd()
            result += SEP
            result += SEP

        for trg in sorted(self.Triggers, key=lambda x: x.FullName):
            result += trg.QueryAdd()
            result += SEP
            result += SEP

        return result.strip() + SEP


def QueryTable(version):
    if version in (9, 9):
        return """
            SELECT
                c.oid,
                trim(lower(n.nspname)) AS schema,
                trim(lower(c.relname)) AS name,
                trim(lower(r.rolname)) AS owner,
                trim(upper(c.relhasoids::varchar)) as has_oids,
                obj_description(c.oid) AS comment,
                case
                    when coalesce(trim(pc.relname), '') = '' then null
                    else pn.nspname || '.' || pc.relname
                end AS parent_table,
                null::varchar as part_border,
                null::varchar as part_key,
                c.relacl,
                c.reloptions
            FROM pg_class c
            JOIN pg_namespace n ON
                n.oid = c.relnamespace
            JOIN pg_roles r ON
                r.oid = c.relowner
            LEFT JOIN pg_inherits inh ON
                c.oid = inh.inhrelid
            LEFT JOIN pg_class pc ON
                pc.oid = inh.inhparent
            LEFT JOIN pg_namespace pn ON
                pn.oid = pc.relnamespace
            WHERE
                c.relkind in ('r','p') AND
                n.nspname != ALL(%s)
            ORDER BY 2,3
        """
    elif version in (10,11):
        return """
            SELECT
                c.oid,
                trim(lower(n.nspname)) AS schema,
                trim(lower(c.relname)) AS name,
                trim(lower(r.rolname)) AS owner,
                trim(upper(c.relhasoids::varchar)) as has_oids,
                obj_description(c.oid) AS comment,
                case
                    when coalesce(trim(pc.relname), '') = '' then null
                    else pn.nspname || '.' || pc.relname
                end AS parent_table,
                pg_get_expr(c.relpartbound, c.oid, true) as part_border,
                pg_get_partkeydef(c.oid) as part_key,
                c.relacl::varchar[],
                c.reloptions
            FROM pg_class c
            JOIN pg_namespace n ON
                n.oid = c.relnamespace
            JOIN pg_roles r ON
                r.oid = c.relowner
            LEFT JOIN pg_inherits inh ON
                c.oid = inh.inhrelid
            LEFT JOIN pg_class pc ON
                pc.oid = inh.inhparent
            LEFT JOIN pg_namespace pn ON
                pn.oid = pc.relnamespace
            WHERE
                c.relkind in ('r','p') AND
                n.nspname != ALL(%s)
            ORDER BY 2,3
        """
    elif version in (12,12):
        return """
            SELECT
                c.oid,
                trim(lower(n.nspname)) AS schema,
                trim(lower(c.relname)) AS name,
                trim(lower(r.rolname)) AS owner,
                false::varchar as has_oids,
                obj_description(c.oid) AS comment,
                case
                    when coalesce(trim(pc.relname), '') = '' then null
                    else pn.nspname || '.' || pc.relname
                end AS parent_table,
                pg_get_expr(c.relpartbound, c.oid, true) as part_border,
                pg_get_partkeydef(c.oid) as part_key,
                c.relacl::varchar[],
                c.reloptions
            FROM pg_class c
            JOIN pg_namespace n ON
                n.oid = c.relnamespace
            JOIN pg_roles r ON
                r.oid = c.relowner
            LEFT JOIN pg_inherits inh ON
                c.oid = inh.inhrelid
            LEFT JOIN pg_class pc ON
                pc.oid = inh.inhparent
            LEFT JOIN pg_namespace pn ON
                pn.oid = pc.relnamespace
            WHERE
                c.relkind in ('r','p') AND
                n.nspname != ALL(%s)
            ORDER BY 2,3
        """
