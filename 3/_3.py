import math
import random
while True:
    s = input("Sign (+, -, *, /, **, rand, fact, acos, mod): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/', '**', 'rand', 'fact', 'acos', 'mod'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print("%.2f" % (a + b))
        elif s == '-':
            print("%.2f" % (a - b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s == '**':
            print("%.2f" % (a ** b))
        elif s == 'rand':
            print("%.2f" % random.randint(a, b))
        elif s == 'fact':
            print("%.2f" % math.factorial(a, b))
        elif s == 'acos':
            print("%.2f" % math.acos(a, b))
        elif s == 'mod':
            print("%.2f" % (a % b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("Division by zero!")
    else:
        print("Invalid operation sign!")
