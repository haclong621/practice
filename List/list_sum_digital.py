l = [12, 67, 98, 34]


def s1():
    m = []
    for i in l :
        for b in range(0,10):
            for a in range(0,10):
                if i == 10*a + b:
                    m.insert(i, a+b) 
    print('#1: ', m)
s1()
    
    
def s2():
    l2 = l.copy()
    r = range(0,10)
    for i in range(0, len(l2)):
        for a in r:
            for b in r:
                if l2[i] == 10*a + b:
                    l2[i] = a + b
    print('#2: ', l2)
s2()



def s3():
    res = []
    for ele in l:
        x = 0
        for digit in str(ele):
            x += int(digit)
        res.append(x)
    print ("#3: ", res)
s3()


def s4():

    from functools import reduce 
    l4 = [reduce(lambda a , b : int(a) + int(b) , list(str(j))) for j in l] 
    print('#4: ', str(l4))
s4()

def s5():
   
    l5 = map(lambda a: sum(int(digit) for digit in str(a)), l) 
    
    print('#5: ', list(l5))
s5()
