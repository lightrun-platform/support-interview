import os
import time
import requests

SERVER_URL = os.getenv('SERVER_URL', 'http://localhost:5000')

while True:
    try:
        response = requests.get(SERVER_URL)
        print("Successfully connected")
    except requests.exceptions.RequestException as err:
        print("Connection failed, {}".format(err))
    time.sleep(5)
