L = [1,2,3,4,5]

newlist = [L[len(L)-i] for i in range(1,len(L)+1)]

print(newlist)
    
def rev():
    L1 = L.copy()
    L2 = []
    for i in L1:
        L2.insert(0,i)
    print(L2)
rev()


def rev1():
    L3 = L.copy()
    L4 = L3[::-1]
    print(L4)
rev1()

def rev3():
    L5 = L.copy()
    L6 = []
    k = L5.pop()
    if L5 != 0:
        L6.append(L5.pop())
    else:
        print(L6)
rev3()
    