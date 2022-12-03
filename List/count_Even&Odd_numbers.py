l = [2, 7, 5, 64, 14,2]

def count1():
    E = []
    O = []
    for c1 in l:
        if c1 % 2 == 0:
            E.append(c1)
        else: 
            O.append(c1)
            
    print('E : ', len(E))
    print('O : ', len(O))
count1()


l2 = l.copy()
for i in range(0, len(l2)):
    if l2[i] % 2 == 0:
        l2[i] = 2
    else:  
        l2[i] = 1
        
print('E: ',l2.count(2))
print('O: ',l2.count(1))



            