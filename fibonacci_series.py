#! /usr/bin/python -v

'''
Fibonacci series: Fibonacci is a series of intergers starting with 0 and 1.
Series continues by adding preceeding two numbers
'''

input_value = int(input('How many numbers you want in the fibonacci series?'))

if(input_value < 0):
    print('enter a valid number')
    exit(0)
else:
    a, b = 0, 1
    sum = 0
    for i in range(input_value):
        a = b
        b = sum
        print(sum, end=',')
        sum = a + b
    print (' - fibonacci series up to', input_value )