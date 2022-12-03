a = int(input('nhap a: '))
b = int(input('nhap b: '))

def max1():
    if a > b:
        print('max: ', a)
    else:
        print('max: ', b)
max1()

def max2():
    print('max: ', max(a,b))
max2()

def min1():
    print('min: ' , min(a,b))
min1()

def min2():
    if a > b:
        print('min: ', b)
    else: print('min: ' + a)
min2()