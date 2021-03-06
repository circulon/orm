import unittest

from src.masoniteorm.query import QueryBuilder
from src.masoniteorm.query.grammars import MSSQLGrammar


class TestMySQLInsertGrammar(unittest.TestCase):
    def setUp(self):
        self.builder = QueryBuilder(MSSQLGrammar, table="users")

    def test_can_compile_insert(self):

        to_sql = self.builder.create({"name": "Joe"}, query=True).to_sql()

        sql = "INSERT INTO [users] ([users].[name]) VALUES ('Joe')"
        self.assertEqual(to_sql, sql)
