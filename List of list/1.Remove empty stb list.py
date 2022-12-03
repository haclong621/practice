l = [5, 6, [], 3, [],[], 9]

def r1():
    l1 = []
    for i in l:
        if type(i) == int:
            l1.append(i)
    print(l1)
r1()


def r2():
    r22 = list(filter(None, l))
    print(r22)
r2()

def r3():
    r33 = []
    for i in l :
        if (str(i).isdigit()) == True:
            r33.append(i)
    print(r33)
r3()