l = [4, 5, 6, 7, 3, 9]
max = 10
min = 5

def t1():
    t11 = []
    for a in l:
        if a >= min and a < max :
            t11.append(1)
        else: t11.append(0)
    #print(t11)
    import math
    if math.prod(t11) == 0:
        print (False)
    else : print (True)
t1()

#def t2():
#    res = True
#    for a in l:
#        if a < min and a >= max:
#            res = False
#            break
#    print(str(res))
#t2()

def t3():
    i = all(a >= min and a < max for a in l)
    print(i)
t3()