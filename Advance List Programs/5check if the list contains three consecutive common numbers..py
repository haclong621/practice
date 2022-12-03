l = [1, 1, 1, 64, 23, 64, 22, 22, 22]

def c1():
    res = []
    for a in l:
        if l.count(a) == 3:
            res.append(a)
    print(set(res))
c1()

