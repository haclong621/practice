a = 4
b = 15
l = list(range(a,b))

def r1():
    r11 = l.copy()
    for i in r11:
        if  i % 2 == 0:
            i == i 
        else: r11.remove(i)
    print(r11)
r1()


def r2():
    r22 = []
    n = a
    while n < b:
        if n % 2 == 0: r22.append(n)
        n = n + 1
    print (r22)
r2()


