l =  [1, 1, 2, 3, 4, 5, 1, 2, 1, 2, 1, 3]
#Output : 2 3 4 5 2

def r1():
    l1 = []
    for a in l:
        if l.count(a) == 1:
            l1.append(a)
    print(l1)
r1()