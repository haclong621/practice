l = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3 
# [4, 3] 


def e1():
    l1 = list(set(l))
    for a in l1:
        count = l.count(a)
        if count > k:
            print(a)

e1()

def e2():
    l2 = list(input())
    k1 = int(input())
    print(l2)
    print(k1)
    l22 = list(set(l2))
    for a in l22:
        count = l2.count(a)
        if count > k1:
            print(a)
e2()
