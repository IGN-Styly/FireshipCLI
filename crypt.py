import rsa #CRYPT Client edition

def load_keys():
    with open('public.pem', 'rb') as f:
        public_key=rsa.PublicKey.load_pkcs1(f.read())
    f.close()
    return public_key

def encrypt(data):
    return rsa.encrypt(data, pub_key=load_keys())
