
#import du bib math

from math import *

print('f(x,y) = x²y - xy²')

#Saisie et controle de saisie sur les valeur de x et y

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

#Calculer le gradient

f1 = 2 * x * y - pow(y, 2)
f2 = pow(x, 2) - 2 * y * x

print('the value of the gradient is : ', '\n', f1, '\n', f2)

# Coded by Med Hedi Ben Atig
