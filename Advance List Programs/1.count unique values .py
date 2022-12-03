l = [1, 2, 2, 5, 8, 4, 4, 8]

def c1():
    l1 = range (min(l), max(l)+1)
    l11 = []
    for a in l1:
        if a in l:
            l11.append(a)
    print('#1: ', len(l11))
c1()

def c2():
    import collections
    a = collections.Counter(l)
    b = (list(a.items()))
    print('#2: ', len(b))
c2()


def c3():
    print('#3: ',len(set(l)))

c3()

def c4():
    n = 0
    c = []
    for a in l:
        if a not in c:
            n += 1
            c.append(a)
    print(n)
c4()