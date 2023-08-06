#!/usr/bin/python
# -*- coding: utf-8 -*-

from pg_metadata._System import SEP
from pg_metadata.ACL     import ACL
from pg_metadata.Owner   import Owner
from pg_metadata.Comment import Comment

QUERY_VIEW = """
    SELECT
        c.oid,
        trim(lower(n.nspname)) AS schema,
        trim(lower(c.relname)) AS name,
        trim(lower(r.rolname)) AS owner_name,
        trim(coalesce(obj_description(c.oid), '')) AS comment,
        pg_get_viewdef(c.oid, true) as definition,
        c.relacl::varchar[],
        c.relkind = 'm' as is_materialized
    FROM pg_class c
    JOIN pg_namespace n ON
        n.oid = c.relnamespace AND
        n.nspname != ALL(%s)
    JOIN pg_roles r ON
        r.oid = c.relowner
    WHERE c.relkind in ('v','m')
    ORDER BY 2,3
"""

class View():
    def __init__(self, row={}, ddl_style=""):
        assert row is not None
        assert isinstance(row, dict)
        assert len(row.keys()) > 0

        self.Oid = row.get('oid')
        assert self.Oid is not None and self.Oid > 0

        self.Schema = row.get('schema') or ''
        self.Schema = self.Schema.strip()
        assert len(self.Schema) > 0

        self.Name = row.get('name') or ''
        self.Name = self.Name.strip()
        assert len(self.Name) > 0

        self.FullName = "%s.%s" % (self.Schema, self.Name)

        self.Definition = row.get('definition') or ''
        self.Definition = self.Definition.strip()
        assert len(self.Definition) > 0

        self.IsMaterialized = row.get("is_materialized")

        if self.IsMaterialized:
            self.Type = "MATERIALIZED VIEW"
        else:
            self.Type = "VIEW"

        self.Folder = "view"

        self.DDLStyle = ddl_style

        self.Owner = Owner(
            "TABLE",
            self.FullName,
            row.get("owner_name"),
            self.DDLStyle
        )

        self.Comment = Comment(
            self.Type,
            self.FullName,
            row.get("comment"),
            self.DDLStyle
        )

        self.ACL = ACL(
            "TABLE",
            self.FullName,
            self.Owner.Owner,
            row.get("relacl"),
            self.DDLStyle
        )

        self.Indexes = []

    def __str__(self):
        return self.FullName

    def QueryAdd(self):
        r = ""

        if self.IsMaterialized:
            r += "CREATE MATERIALIZED VIEW %s AS" % (self.FullName)
        else:
            r += "CREATE OR REPLACE VIEW %s AS" % (self.FullName)
        r += SEP
        r += self.Definition

        return r

    def QueryRemove(self):
        if self.IsMaterialized:
            return 'DROP MATRIALIZED VIEW IF EXISTS %s.%s;' % (self.Schema, self.Name)
        else:
            return 'DROP VIEW IF EXISTS %s.%s;' % (self.Schema, self.Name)

    def QueryDDL(self):
        result = ''
        result += self.QueryRemove()
        result += SEP
        result += SEP
        result += self.QueryAdd()
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

        for ind in self.Indexes:
            result += ind.QueryAdd()
            result += SEP
            result += SEP

        return result.strip() + SEP
