import unittest

import sqlglot
from asthash.asthash import parse_sql_to_ast, modify_ast_with_hash, rebuild_sql_from_ast, hash_column_name


class TestSQLModification(unittest.TestCase):

    def test_hash_column_name(self):
        column_name = "test"
        hash_result = hash_column_name(column_name)
        self.assertEqual(hash_result, "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")

    def test_parse_sql_to_ast(self):
        sql_query = "SELECT a, b FROM test WHERE a = 5;"
        ast = parse_sql_to_ast(sql_query)
        self.assertIsNotNone(ast)

    def test_modify_ast_with_hash(self):
        sql_query = "SELECT a, b FROM test WHERE a = 5;"
        ast = parse_sql_to_ast(sql_query)
        modified_ast, column_mapping = modify_ast_with_hash(ast)
        self.assertIsNotNone(modified_ast)
        self.assertDictEqual(column_mapping, {"a": hash_column_name("a"), "b": hash_column_name("b")})

    def test_modify_ast_with_hash_uppercase(self):
        sql_query = "SELECT test.a FROM test WHERE test.a = 5 ORDER BY b, A;"
        ast = parse_sql_to_ast(sql_query)
        modified_ast, column_mapping = modify_ast_with_hash(ast)
        self.assertIsNotNone(modified_ast)
        self.assertDictEqual(column_mapping, {"a": hash_column_name('a'), "b": hash_column_name("b")})

    def test_rebuild_sql_from_modified_ast(self):
        sql_query = "SELECT a, b FROM test WHERE a = 5;"
        ast = parse_sql_to_ast(sql_query)
        modified_ast, _ = modify_ast_with_hash(ast)
        rebuilt_sql = rebuild_sql_from_ast(modified_ast)
        self.assertEqual(rebuilt_sql, f"SELECT {hash_column_name('a')}, {hash_column_name('b')} FROM test WHERE {hash_column_name('a')} = 5")

    def test_parse_sql_to_ast_error(self):
        sql_query = "SELECT a, b FROM"
        with self.assertRaises(sqlglot.errors.ParseError):
            parse_sql_to_ast(sql_query)


if __name__ == '__main__':
    unittest.main()
