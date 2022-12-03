tl1 = [ [1, 2], [3, 4], [5, 6] ]
tl2 = [ [3, 4], [5, 7], [1, 2] ]

def u1():
    u11 = []
    for a in tl1:
        if a not in tl2:
            u11.append(a)
    for a in tl2:
        if a not in tl1:
            u11.append(a)
            
    print(u11)
u1()


def u2():
    a = (set(map(tuple,tl1)))
    b = (set(map(tuple,tl2)))
    c = map(list,(a ^ b))
    print(list(c))
u2()