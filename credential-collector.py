import requests
import random
import time
import os

COLLECTOR_TARGETS = [
    "https://legitimate-site.com/login",
    "https://corporate-login.com/auth"
]

def collect_credentials():
    while True:
        for target in COLLECTOR_TARGETS:
            username = f"user{random.randint(10000, 99999)}"
            password = f"pass{random.randint(10000, 99999)}"
            
            try:
                requests.post(target, data={
                    'username': username,
                    'password': password
                })
                
                time.sleep(random.uniform(0.1, 1.0))
            except:
                continue

if __name__ == '__main__':
    collect_credentials()
