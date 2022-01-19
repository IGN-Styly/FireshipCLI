import requests
import json
import creds
import base64
token=creds.token
TRKEY=creds.TRKEY
val=creds.val
url="http://127.0.0.1:5000/send?token={}&TRKEY={}&val={}".format(token, TRKEY, val)
a=requests.post(url=url)
print(a.text)