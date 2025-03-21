"""
     Practice creating Python programs to perform arithmetic and string, experimenting with variables, and exploring data types
"""
a = int(input('enter your first number: '))
b = int(input('enter your second number: '))

option = input('choose your math sysmbol: [+, -, /, *]\n')
if option == '+':
    results = a + b
    print(f'The addition of  {a} + {b} = {results}')

elif option == '-':
    results = a - b
    print(f'The subtraction of  {a} -/ {b} = {results}')

elif option == '/':
    results = a / b
    print(f'The division of  {a} / {b} = {results}')

elif option == '*':
    results = a * b
    print(f'The multiplication of  {a} * {b} = {results}')

else:
    print('Wrong option, read and try again')