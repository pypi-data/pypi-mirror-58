from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import HMAC, SHA512
from base64 import b64encode
from base64 import b64decode

#def sign_data()

f = open('key1.private.pem','r')
rsa_private = RSA.import_key(f.read())


data_to_sign = bytes([1,2,3,4,5,6,7,8])
#hashed_message = SHA1.new(data_to_sign)
hashed_message = SHA512.new(data_to_sign)
signature = pkcs1_15.new(rsa_private).sign(hashed_message)
print(signature.hex())

#Verification Test
f = open('key1.public.pem','r')
rsa_public = RSA.import_key(f.read())

try:
    verification_result = False
    pkcs1_15.new(rsa_public).verify(hashed_message, signature)
    verification_result = True
except (ValueError, TypeError):
    verification_result = False

print("verification_result",verification_result)



#>>> message = 'To be signed'
#>>> key = RSA.import_key(open('private_key.der').read())
#>>> h = SHA256.new(message)
#>>> signature = pkcs1_15.new(key).sign(h)


#print(rsa.publickey().exportKey())