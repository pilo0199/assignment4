from flask import Flask
app = Flask(__name__)

@app.route("/")

def run():
    run='The file ran successfully'
    return run

import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = input('Amount of paswords to generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

