#!/usr/bin/python


# COPYRIGHT :
""" 
originally created by @Gabriellpweb at https://del.dog/ogheppa . 
edited by @alenpaul2001 and added custom password options . 

USAGE   :  
encrypt :  ./secure crypt source destination  
decrypt : ./secure decrypt source destination 

"""

import csv
import sys
import Crypto.Random
from Crypto.Cipher import AES
import hashlib
import base64


# salt size in bytes
SALT_SIZE = 16

# number of iterations in the key generation
NUMBER_OF_ITERATIONS = 20

# the size multiple required for AES
AES_MULTIPLE = 16

VAR_NEED=raw_input("Enter The Password : ")

VAR_VV="'"+VAR_NEED+"'"

PASSWORD =VAR_VV  


def generate_key(password, salt, iterations):
    assert iterations > 0

    key = password + salt

    for i in range(iterations):
        key = hashlib.sha256(key).digest()

    return key


def pad_text(text, multiple):
    extra_bytes = len(text) % multiple
    padding_size = multiple - extra_bytes
    padding = chr(padding_size) * padding_size
    padded_text = text + padding
    return padded_text


def unpad_text(padded_text):
    padding_size = ord(padded_text[-1])
    text = padded_text[:-padding_size]
    return text


def encrypt(plaintext, password):
    salt = Crypto.Random.get_random_bytes(SALT_SIZE)
    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)
    iv = Crypto.Random.new().read(AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad_text(plaintext, AES_MULTIPLE)

    ciphertext = cipher.encrypt(padded_plaintext)

    ciphertext_with_salt = base64.b64encode(iv + salt + ciphertext)

    return ciphertext_with_salt


def decrypt(ciphertext, password):
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    salt = ciphertext[AES.block_size:][:SALT_SIZE]

    ciphertext_sans_salt = ciphertext[AES.block_size+SALT_SIZE:]

    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    padded_plaintext = cipher.decrypt(ciphertext_sans_salt)
    plaintext = unpad_text(padded_plaintext)

    return plaintext


def crypt_csv(src_file, dst_file):
    line = 0
    with open(dst_file, 'w') as csv_dst_file:
        csv_writer = csv.writer(csv_dst_file)
        with open(src_file, 'rb') as csv_src_file:
            csv_reader = csv.reader(csv_src_file, delimiter=',')
            for row in csv_reader:
                if line > 0:
                    for i in range(len(row)):
                        row[i] = encrypt(row[i], PASSWORD)
                csv_writer.writerows([row])
                line += 1


def decrypt_csv(src_file, dst_file):
    line = 0
    with open(dst_file, 'w') as csv_dst_file:
        csv_writer = csv.writer(csv_dst_file)
        with open(src_file, 'rb') as csv_src_file:
            csv_reader = csv.reader(csv_src_file, delimiter=',')
            for row in csv_reader:
                if line > 0:
                    for i in range(len(row)):
                        row[i] = decrypt(row[i], PASSWORD)
                csv_writer.writerows([row])
                line += 1

if sys.argv.__len__() <= 2:
    print "invalid arguments. csvcrypto crypt|decrypt src.csv dest.csv"
    sys.exit(0)

if sys.argv[1] == "crypt":
    crypt_csv(sys.argv[2], sys.argv[3])

elif sys.argv[1] == "decrypt":
    decrypt_csv(sys.argv[2], sys.argv[3])

else:
    print "Unknown option"

