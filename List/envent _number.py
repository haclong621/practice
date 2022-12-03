l = [2, 7, 5, 64, 14]


#1
def en1():
    en11 = []
    for i in l:
        if i % 2 == 0:
            en11.append(i)
            
    print(en11)
en1()

#2
def en2():
    en22 = l.copy()
    for i in l:
        if i % 2 == 1:
            en22.remove(i)
            
    print(en22)
en2()

#3
def en3():
    en33 = []
    for j in range(1 , 1000):
        for i in l:
            if i == 2 * j:
                en33.append(i) 
                
    print(en33)
en3()
        
        
#4
def en4():
    n = 0
    en44 = []
    while n < len(l):
        if l[n] % 2 == 0:
            en44.append(l[n]) 
        n = n + 1
                
    print(en44)
en4()

list1 = [2, 7, 5, 64, 14]
for a,i in enumerate(list1):
  if i%2 == 0:
    print(i,end=" ")

