import rsa # CRYPT Server edition 
import base64

def load_keys():
    with open('public.pem', 'rb') as f:
        public_key=rsa.PublicKey.load_pkcs1(f.read())
    f.close()
    return public_key
pub_key=load_keys()

def encrypt(data):
    return rsa.encrypt(data.encode(), pub_key)