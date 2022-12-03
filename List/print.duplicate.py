l = [1, 2, 3,2, 2, 3, 4, 5, -2, 6, 6, -2, 2]

def d1():
    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)      
        
    #for j in l1:
    #    print(j)
    #    print(l.count(j)) 
    #    if l.count(j) == 1: l1.remove(j) 
#    print(l1)

    print([x for x in l1 if l.count(x) != 1])
 
d1()

def d2():
    l2 = l.copy()
    l22 = []
    for i in l2:
        if l2.count(i) > 1:
            l22.append(i)
    print(list(set(l22)))
d2()

#def d3():
#    l3 = []
#    for i in l:
#        if i not in l3:
#            l3.append(i)      
#        
#    for num in l3:
#        if l.count(num) == 1: l3.remove(num)   
#    print(l3)
#d3()