l = [2, -7, 5, -64, -14]

def c1():
    pos = []
    neg = []
    for c11 in l:
        if c11 > 0:
            pos.append(c11)
        if c11 < 0:
            neg.append(c11)
    print('Positive numbers: ', len(pos))
    print('Negative numbers: ', len(neg))
c1()


def c2():
    l2 = l.copy()
    for i in range(0 , len(l2)):
        if l2[i] > 0:
            l2[i] = 1
        if l2[i] < 0:
            l2[i] = -1
    print('Positive numbers: ', l2.count(1))
    print('Positive numbers: ', l2.count(-1))
c2()


def c3():
    pos, neg = 0, 0
    for i in l:
        if i > 0:
            pos = pos + 1
        if i < 0:
            neg = neg + 1
            
    print('Positive numbers: ', pos)
    print('Negative numbers: ', neg)
c3()


def c4():
    l4 = l.copy()
    pos = list(map(lambda x: 1 if x > 0 else -1, l4))
    print('#4')
    print('Positive numbers: ', pos.count(1))
    print('Positive numbers: ', pos.count(-1))
c4()