L1 = [1,2,3,4,5]
L2 = [6,7,8,9]
p1 = 1
p2 = 3
p3 = 2
p4 = 5

#print('#1')                     #1
#print(L1)
#def swap1():
    #a = L1.copy()
    #b = p1
    #c = p2
    
    #a[b] , a[c] = a[c] , a[b]
    
    #print('=> ',a)
#swap1()

#print('#2')                     #2
#def swap2():
    #a = L2.copy()
    #b = p3 - 1
    #c = p4 - 3
    
    #a[b] , a[c] = a[c] , a[b]
    #print('=> ',a)
#swap2() 
    
def CT():
    a = L1.copy()
    b = L2.copy()
    c = d = 0
    for i in a:
        c = c + 1
    print('a = ', str(c))
    
    for j in b:
        d = d + 1
    print('b = ', str(d))
CT()

def ct1():
    a = len(L1.copy())
    b = len(L2.copy())
    
    print('a1 = ', a)
    print('b1 = ', b)
ct1()

def ct2():
    a = L1.copy()
    b = L2.copy()
    
    
    c = sum(1 for i in a)            
    d = sum(1 for j in b)
    
   
    print('a2 = ' , c)
    print('b2 = ' , d)
ct2()
    

    
    

    
    



