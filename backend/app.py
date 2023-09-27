from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from asthash.asthash import parse_sql_to_ast, modify_ast_with_hash, rebuild_sql_from_ast

app = Flask(__name__)
CORS(app)  # Enable CORS for the app


# Initialize SQLite database


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


conn = get_db_connection()
conn.execute('CREATE TABLE IF NOT EXISTS mapping (original text, hashed text)')
conn.commit()
conn.close()


def get_column_mapping():
    try:
        conn = get_db_connection()
        mapping_rows = conn.execute('SELECT original, hashed FROM mapping').fetchall()
        conn.close()
        return dict(mapping_rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Define API endpoints for parsing, modifying, and rebuilding SQL queries


@app.route('/parse', methods=['POST'])
def parse_sql():
    try:
        sql_query = request.get_json()['query']
        if ast := parse_sql_to_ast(sql_query):
            return jsonify({"ast": repr(ast)})

        return jsonify({"error": "Failed to parse SQL."}), 400

    except Exception:
        return jsonify({"error": f"Failed to parse '{sql_query}'"}), 500


@app.route('/modify', methods=['POST'])
def modify_sql():
    sql_query = request.get_json()['query']
    try:
        if ast := parse_sql_to_ast(sql_query):
            modified_ast, mapping = modify_ast_with_hash(ast)

            # Store the mapping in the SQLite database
            columns_stored = get_column_mapping()
            conn = get_db_connection()
            for original, hashed in mapping.items():
                if original not in columns_stored:
                    conn.execute('INSERT INTO mapping (original, hashed) VALUES (?, ?)', (original, hashed))
            conn.commit()
            conn.close()

            return jsonify({"modified_ast": repr(modified_ast), "mapping": mapping})

        return jsonify({"error": "Failed to modify AST."}), 400

    except Exception:
        return jsonify({"error": f"Failed to modify AST of '{sql_query}'"}), 500


@app.route('/rebuild', methods=['POST'])
def rebuild_sql():
    try:
        sql_query = request.get_json()['query']
        if ast := parse_sql_to_ast(sql_query):
            modified_ast, mapping = modify_ast_with_hash(ast)
            rebuilded_sql = rebuild_sql_from_ast(modified_ast)
            return jsonify({"rebuilded_sql": rebuilded_sql, "mapping": mapping})

        return jsonify({"error": "Failed to parse SQL."}), 400

    except Exception:
        return jsonify({"error": f"Failed to rebuild '{sql_query}'"}), 500


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
