import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

print('Hello, I will help you to generate a password for you, but now answer to questions, which will help me to help you :)')
print('How much passwords do you need?')
count = input()
print('Write please Length of your password')
length = int(input())
digits = input('Digits - 0123456789? - yes/no: ')

up_letters = input('Upper letters - ABCDEFGHIJKLMNOPQRSTUVWXYZ? - yes/no: ')

low_letters = input('Lower letters -  abcdefghijklmnopqrstuvwxyz? - yes/no: ')

symbols = input('Symbols - !#$%&*+-=?@^_?  - yes/no: ')

ex_simbols = input('Ambiguous symbols? - il1Lo0O? - yes/no: ')
