lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10 #int(input('Nhap x: '))
y = 15 #int(input('Nhap y: '))

#1
def c1():
    print('#1: x = ', lst.count(x), 'y = ', lst.count(y))
c1()


#2
def c2():
    n = 0
    m = 0
    
    for i in lst:
        if i == x:
            n = n+1
    
        if i == y:
            m = m+1
               
            
    print('#2: x = ', n , 'y = ' , m )
c2()


#3
def c3():
    l3 = lst.copy()
    l33 = lst.copy()
    
    for i in lst:
        if x == i:
            l3.remove(i)
            
        if y == i:
            l33.remove(i)
       
    print('#3: x = ', len(lst)-len(l3),  'y = ' , len(lst)-len(l33))
c3()


#4
def c4():
    l4 = lst.copy()
    l44 = lst.copy()
    
    for i in lst:
        if x != i:
            l4.remove(i)       
    
        if y != i:
            l44.remove(i)
         
    print('#4: x = ', len(l4) , 'y = ', len(l44))
c4()


#5

#import pandas

#l5 = lst.copy()
   
#count = pd.Series(l5).value_counts()
#print("Element Count")