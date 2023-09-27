import hashlib
import sqlglot


def parse_sql_to_ast(sql_query):
    """
    Parse the SQL query to an Abstract Syntax Tree (AST) using sqlglot.

    Args:
        sql_query (str): The SQL query to parse.

    Returns:
        dict: The parsed AST.
    """
    return sqlglot.parse_one(sql_query)


def modify_ast_with_hash(ast):
    """
    Modify the AST by hashing column names and maintain a mapping of original column names to hashed column names.

    Args:
        ast (sqlglot.ast.Select): The AST representation of the SQL query.

    Returns:
        sqlglot.ast.Select: The modified AST.
        dict: A mapping of original column names to hashed column names.
    """

    # def proces_node(node, column_mapping):
    #     if isinstance(node, sqlglot.):
    #         column_name = node.name
    #         hashed_column = f"<hashed column name of {column_name}>"
    #         column_mapping[column_name] = hashed_column
    #         node.name = hashed_column

    #     for child in node.children:
    #         proces_node(child, column_mapping)

    column_mapping = {}

    # proces_node(ast, column_mapping)

    for column in ast.find_all(sqlglot.exp.Column):
        column_name = column.alias_or_name.lower()
        if column_name not in column_mapping:
            hashed_column = hash_column_name(column_name)
            column_mapping[column_name] = hashed_column
        column.set("this", column_mapping[column_name])

    return ast, column_mapping


def hash_column_name(column_name):
    hash_object = hashlib.sha256(column_name.encode("utf8"))
    return hash_object.hexdigest()


def rebuild_sql_from_ast(modified_ast):
    """
    Rebuild the SQL query from the modified AST.

    Args:
        modified_ast (sqlglot.ast.Select): The modified AST.

    Returns:
        str: The SQL query string with hashed column names.
    """
    return modified_ast.sql()
