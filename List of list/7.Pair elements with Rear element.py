l = [[4, 5, 6, 8], [2, 4, 5], [6, 7, 5]]
rs = [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]

def p1():
    l1 = l.copy()
    l11 = []
    for a in l1:
        for x in range (0, len(a)-1):
                l11.append(list([a[x], a[x+1]]))
       
    print('#1: ',l11)
p1()


def p2():
    l1 = l.copy()
    l11 = []
    for a in l1:
        l11.append(list([a[x], a[x+1]] for x in range (0, len(a)-1)))
       
    print('#2: ',l11)
p2()
        

res = []
for sub in l:
    res.append([[ele, sub[-1]] for ele in sub[:-1]])
    
print ('#3: ',str(res))


from itertools import product
def p4():
    from itertools import product
    l3 = l.copy()
    l33 = []
    for a in l3:
        l33.append(list(product(a[:-1],[a[-1]])))
    print('#4: ',l33)
p4()
