import click
from asthash.asthash import parse_sql_to_ast, modify_ast_with_hash, rebuild_sql_from_ast


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--action', type=click.Choice(['parse', 'modify', 'rebuild']), help='Choose action: parse, modify or rebuild')
@click.option('--sql-query', help='Enter the SQL query')
def main(action, sql_query):
    if action == 'parse':
        if ast := parse_sql_to_ast(sql_query):
            click.echo("AST Representation:")
            click.echo(repr(ast))
        else:
            click.echo("Failed to parse SQL.")

    elif action == 'modify':
        ast = parse_sql_to_ast(sql_query)
        modified_ast, column_mapping = modify_ast_with_hash(ast)
        click.echo("Modified AST:")
        click.echo(repr(modified_ast))
        click.echo("Column Mapping:")
        click.echo(column_mapping)

    elif action == 'rebuild':
        ast = parse_sql_to_ast(sql_query)
        modified_ast, column_mapping = modify_ast_with_hash(ast)
        rebuilt_sql = rebuild_sql_from_ast(modified_ast)
        click.echo("Rebuilded SQL:")
        click.echo(rebuilt_sql)


if __name__ == "__main__":
    main()
