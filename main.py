# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from math import *

print('f(x,y) = x²y - xy²')

while True:
    try:
        x = float(input("Please enter the value of X : "))
        break
    except ValueError:
        print("X must be a numeric value")

while True:
    try:
        y = float(input("Please enter the value of Y : "))
        break
    except ValueError:
        print("Y must be a numeric value")

f1 = 2 * x * y - pow(y, 2)
f2 = pow(x, 2) - 2 * y * x

print('the value of the gradient is : ', '\n', f1, '\n', f2)

