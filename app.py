from flask import Flask, request, render_template, redirect, url_for
import pyodbc

app = Flask(__name__)

# Connect to SQL Server
def get_db_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=WANI-SOB\\MSSQLSERVER01;"
        "DATABASE=;"
        "UID=sa;"
        "PWD=Server@123"
    )
    conn = pyodbc.connect(conn_str)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    roll_no = request.form.get('roll_no')
    
    if name and roll_no:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO render1 (name, roll_no) VALUES (?, ?)"
            cursor.execute(query, (name, roll_no))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('index', success=True))
        except Exception as e:
            return f"Error: {e}", 500
    return "Name and Roll Number are required.", 400

if __name__ == '__main__':
    app.run(debug=True)
