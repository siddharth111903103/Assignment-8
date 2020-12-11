try :
    print(1/0)
except ZeroDivisionError :
    print("number cannot be divided by zero")

try :
    print(5 + '5')
except TypeError :
    print("cannot add integer to string")

try :
    print(a + b*3)
except NameError :
    print("variables a and b are not defined")