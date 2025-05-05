from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize the fake customer database
def init_db():
    conn = sqlite3.connect("cryptobank_data.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS clients")
    cur.execute("CREATE TABLE clients (id INTEGER PRIMARY KEY, name TEXT, balance REAL, wallet TEXT)")
    cur.execute("INSERT INTO clients (name, balance, wallet) VALUES ('Alice', 3.2, '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')")
    cur.execute("INSERT INTO clients (name, balance, wallet) VALUES ('Bob', 5.5, '3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy')")
    cur.execute("INSERT INTO clients (name, balance, wallet) VALUES ('Eve', 0.01, 'bc1qw508d6qejxtdg4y5r3zarvary0c5xw7k6j28z')")
    conn.commit()
    conn.close()

# HTML Template with black background
template = """
<!DOCTYPE html>
<html>
<head>
    <title>CryptoBank Data Lookup</title>
    <style>
        body {
            background-color: black;
            color: #00ff99;
            font-family: monospace;
        }
        input, button {
            background-color: #111;
            color: #00ff99;
            border: 1px solid #00ff99;
            padding: 5px;
        }
    </style>
</head>
<body>
    <h1>CryptoBank Client Data Lookup</h1>
    <form method="GET" action="/search">
        <label>Client name:</label>
        <input type="text" name="name">
        <button type="submit">Search</button>
    </form>
    <pre>{{ output }}</pre>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template, output="")

@app.route('/search')
def search():
    name = request.args.get('name', '')
    output = ''
    if name:
        query = f"SELECT * FROM clients WHERE name = '{name}'"
        try:
            conn = sqlite3.connect("cryptobank_data.db")
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            conn.close()
            if rows:
                output = '\n'.join([f"ID: {r[0]}, Name: {r[1]}, Balance: {r[2]} BTC, Wallet: {r[3]}" for r in rows])
            else:
                output = "No client found."
        except Exception as e:
            output = f"SQL Error: {str(e)}"
    return render_template_string(template, output=output)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
