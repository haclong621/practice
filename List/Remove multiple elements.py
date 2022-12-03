l = [11, 5, 17, 18, 23, 50]


def r1():
    l1 = l.copy()
    for i in reversed(range(0, len(l))):
        if i % 2 == 0:
            print(l1[i], end = " ")
            del l1[i]
    print(l1)
r1()

def r2():
    rem = []
    newl = []
    
        
    for i in range(0, len(l)):
        if i % 2 == 0:
            rem.append(l[i])
        else: newl.append(l[i])
    print(rem)
    print(newl)
r2()