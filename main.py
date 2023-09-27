import click
from asthash.asthash import parse_sql_to_ast, modify_ast_with_hash, rebuild_sql_from_ast


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--action', type=click.Choice(['parse', 'modify']), help='Choose action: parse or modify')
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
        rebuilt_sql = rebuild_sql_from_ast(modified_ast)
        click.echo("Modified SQL:")
        click.echo(rebuilt_sql)
        click.echo("Column Mapping:")
        click.echo(column_mapping)


if __name__ == "__main__":
    main()
