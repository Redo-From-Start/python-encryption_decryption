import sys
import random
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

print("do you want to (E)ncrypt or (D)ecrypt")
c = input()
if c == "E":
    print('password:')
    password_provided = input() # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes
    salt = b"b\xfb/\x05\xe3p\x0c\\\xda\x14\xbe\x18|z4\xca\x19" # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    d = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    print('msg:')
    message = input().encode()
    key = Fernet(d)
    encrypted = key.encrypt(message)
    f = open('out.enc', 'wb+')
    f.write(encrypted)
    f.close()
elif c == "D":
    print('file:')
    f = open(input(),'rb')
    decrypt = f.read() # The key will be type bytes
    f.close()
    print('password:')
    password_provided = input() # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes
    salt = b"b\xfb/\x05\xe3p\x0c\\\xda\x14\xbe\x18|z4\xca\x19" # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    d = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    f = Fernet(d)
    decrypted = f.decrypt(decrypt)
    f = open('out.unc','wb+')
    f.write(decrypted)
    f.close()
else:
    print("ERROR")
    sys.exit()