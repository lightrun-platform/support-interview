import os
import requests

SERVER_URL = os.getenv('SERVER_URL', 'http://server:8080')

while True:
    try:
        response = requests.get(SERVER_URL)
        print("Successfully connected")
    except requests.exceptions.RequestException as err:
        print ("Connection failed")
    time.sleep(3)
