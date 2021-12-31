import re
from random import SystemRandom
import json
import random

def affine_encrypt(text, key):
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])

def affine_decrypt(cipher, key):
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

encrypt = open('json/Encrypt.json', 'r')
encryptdata = encrypt.read()

operation = open('json/Encrypt.json', 'r')
operation = operation.read()

decrypt = open('json/Encrypt.json', 'r')
decryptdata = decrypt.read

with open('json/encrypt.json', 'r') as f:
    json_data = json.load(f)

with open('json/Encrypt.json', 'r') as f:
    json_data = json.load(f)
for a in 'json/Encrypt.json':
    num = re.findall(r"\d+", 'key1' + 'key2')
    break

with open('json/Encrypt.json', 'w') as f:
    f.write(json.dumps(json_data))

obj = json.loads(encryptdata)
cryptogram = json.loads(encryptdata)
operation = (str(obj['operation']))

key1 = (int(obj['a']))
key2 = (int(obj['b']))
print('a and b keys are:', key1, key2)

obj = json.loads(encryptdata)

#if str(obj['operation']): dziala
#str(obj['operation']):dziala z if
if str(obj['operation']):
        text = (str(obj['plainText']))
        key = [key1, key2]

        affine_encrypted_text = affine_encrypt(text, key)

        print('Encrypted Text: {}'.format(affine_encrypted_text))

        with open('output.json', 'a') as f:
            f.write(format(affine_encrypted_text) + '\n')

else:
        text = (str(str(obj['plainText'])))
        key = [key1, key2]

        affine_encrypted_text = affine_encrypt(text, key)

        print('Decrypted Text: {}'.format
              (affine_decrypt(affine_encrypted_text, key)))

        with open('output.json', 'a') as f:
            f.write(format(affine_decrypt(affine_encrypted_text, key) + '\n'))


