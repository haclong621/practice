l = [3, 2, 4] 



#1
def m1():
    from functools import reduce
    print('#1: ', reduce(lambda a,b: a * b, l))
m1()


#2
def m2():
    l2 = l.copy()
    m = 1
    for i in l2:
        m = m * i
        
    print('#2: ', m)
m2()


#3
num = int(input("Toi da: "))
def m3():
    l3 = []
    from functools import reduce
    for j in range(0,num):
        ele= int(input("Nhap: "))
        l3.append(ele)
    print(l3)
    
    #mul = 0
    print('#3: ' , reduce(lambda c,d: c * d, l3))
        
m3()