import requests
import json
import crypt
import creds
data=crypt.encrypt(creds.json_data.encode('utf-8'))
a=requests.post(url="http://127.0.0.1:5000/send", data=creds.json_data)
print(a.content)