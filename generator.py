import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

print('Hello, I will help you to generate a password for you, but now answer to questions, which will help me to help you :)')
print('How much passwords do you need?')
count = int(input())
print('Write please Length of your password')
length = int(input())
digits_answ = input('Digits - 0123456789? - yes/no: ')

up_letters = input('Upper letters - ABCDEFGHIJKLMNOPQRSTUVWXYZ? - yes/no: ')

low_letters = input('Lower letters -  abcdefghijklmnopqrstuvwxyz? - yes/no: ')

symbols = input('Symbols - !#$%&*+-=?@^_?  - yes/no: ')

ex_simbols = input('Ambiguous symbols? - il1Lo0O? - yes/no: ')

def create_char(chars):
  if digits_answ.lower() == 'yes':
    chars += digits
  if up_letters.lower() == 'yes':
    chars += uppercase_letters
  if low_letters.lower() == 'yes':
    chars += lowercase_letters 
  if symbols.lower() == 'yes':
    chars += punctuation
  if ex_simbols.lower() == 'yes':
    chars = chars.replace('i', '')
    chars = chars.replace('l', '')
    chars = chars.replace('1', '')
    chars = chars.replace('L', '')
    chars = chars.replace('o', '')
    chars = chars.replace('0', '')
    chars = chars.replace('O', '')
  return chars

def generator(length, chars):
  result = ''
  for i in range(0, length):
    result += random.choice(chars)
  return result

chars = create_char(chars)

for _ in range(count):
   password = generator(length, chars)
   print('Generated password:', password)  


