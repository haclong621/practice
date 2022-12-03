l = [['a', 'b', 1, 2, 4, 5], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}

#def f1():
#    for sl in l:
#        for x in range(2, len(sl),2):
#            if (x + 1) < len(sl):
#                rs = {(sl[0], sl[1],):(sl[x], sl[x+1])}
#            print(str(rs))          
#f1()



#(def f2():
#    f22 = []
#    f222 = []
#    for sl in l:
#        rs = [((sl[0], sl[1]) , (sl[x], sl[x+1])) for x in range(2, len(sl), 2)]
#        f22.append(rs)
#    for i in f22:
#        for j in i:
#            f222. append(j)
#    for k in f222:
#        a = [list(k)]
#        b = dict(a)
#        print(b)
#f2())

def f2():
    f22 = []
    rs = dict()
    for sl in l:
        for x in range(2, len(sl), 2):
            #rs[tuple(sl[0:2])] = tuple(sl[x: x+2]) 
            rs[tuple(sl[0:2])]  = (sl[x], sl[x+1])
            print(rs)
  
f2()



#def f3():
#    res = dict()
#    for sub in l:
#        res[tuple(sub[:2])] = tuple(sub[2:])
#    print("The mapped Dictionary : " + str(res)) 
#f3()

