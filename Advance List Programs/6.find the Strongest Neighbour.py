l = [1, 3, 4, 9, 6 , 11, 15, 13, 19]
# > 3 , 4 , 9, 9, 11, 15, ,15, 19

def f1():
    res = []
    for n in range(0, len(l) - 1):
        if l[n] > l[n+1]:
            res.append(l[n])
        else: res.append(l[n+1])
    print(res)
f1()


def f2(l2,n):
    
    l22 = []
    for i in range(0,n-1):
        if l2[i] > l[i+1]:
            l22.append(l2[i])
        else: l22.append(l2[i+1])
    print(l22)
        
if __name__ == "__main__" :
    l2 = l.copy()
    n = 9
    f2(l2,n)
