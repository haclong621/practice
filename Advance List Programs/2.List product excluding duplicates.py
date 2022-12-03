l = [1, 3, 5, 6, 3, 5, 6, 1]



def f1():
    l11 = list(set(l))
    while len(l11) > 1:
        l11[1] = l11[0] * l11[1]
        l11.remove(l11[0])
    print(l11[0])
f1()

def f2():
    l22 = list(set(l))
    for n in range(0, len(l22)-1):
        l22[n+1] = l22[n] * l22[n+1]
    print(l22[-1])
f2()


def f3():
    n = 1
    l33 = []
    for a in l:
        if a not in l33:
            l33.append(a)
            n = n * a
    print(n)
f3()

import functools

def f4():
    import functools
    l4 = list(set(l))
    l44 = functools.reduce(lambda a,b: a*b , l4)
    print(l44)
f4()


print(functools.reduce(lambda x, y: x*y, set([1, 3, 5, 6, 3, 5, 6, 1])))

def f5():
    l5 = set(l)
    import math
    print(math.prod(l5))
f5()