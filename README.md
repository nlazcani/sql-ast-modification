# Documentation

## Task Description
We are tasked with developing a module that can parse PostgreSQL queries, generate an Abstract Syntax Tree (AST), replace column names with hashed values in the AST, maintain a map of original column names to hashed column names, and rebuild the SQL query with hashed column names. This module will also include unit tests to ensure the correctness of our functions.

## Implementation Steps
### Parse SQL to AST:
1. We will use the `sqlparse` library to parse the SQL query string and generate an AST.

### Modify AST:
1. We will traverse the AST and replace all `ColumnRef` elements (column names) with hashed values.
2. We will maintain a map of original column names to hashed column names during this process.

### Rebuild SQL from modified AST:
1. Using the modified AST, we will reconstruct the SQL query string with hashed column names.

### Write Unit Tests:
1. We will write unit tests to verify the correctness of our functions.
2. Test cases will include typical SQL queries and edge cases.


# SQL Query Parser and Modifier

This Python script provides a command-line interface for parsing SQL queries into Abstract Syntax Trees (AST) and modifying those ASTs to rebuild SQL queries.

## Table of Contents

- [Usage](#usage)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [License](#license)

## Usage

To use this script, you must specify the action (`parse` or `modify`) and provide an SQL query.

```bash
# Parsing an SQL query into an AST
python script_name.py --action parse --sql-query "SELECT * FROM table_name"

# Modifying an SQL query using an existing AST
python script_name.py --action modify --sql-query "SELECT * FROM table_name"
```



The script will either parse the SQL query into an AST or modify an existing AST and rebuild the SQL query, depending on the chosen action.
## Requirements
- Python 3.x 
- Additional Python libraries as specified in the script (`parse_sql_to_ast`, `modify_ast_with_hash`, `rebuild_sql_from_ast`)
## Installation 
1. Clone this repository or download the script file. 
2. Install the required Python libraries, if not already installed:

```bash

pip install library_name
``` 
3. Run the script as described in the [Usage](https://chat.openai.com/c/4cbb9b14-94a2-4965-8f28-c9a63e8e01c7#usage)  section.
## Usage Examples 
- Parsing an SQL query into an AST:

```bash

python script_name.py --action parse --sql-query "SELECT * FROM table_name"
``` 
- Modifying an SQL query using an existing AST:

```bash

python script_name.py --action modify --sql-query "SELECT * FROM table_name"
```
## License

This script is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/c/LICENSE)  file for details.

```go

You can replace `script_name.py`, `library_name`, and update the license information accordingly in your actual README documentation.
```