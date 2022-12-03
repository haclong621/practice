l = [20, 10, 20, 4, 100, -125]




l1 = (map(lambda a: abs(a), l))
print(max(list(l1)))

l2 = l.copy()
l21 = []
c = 0
def max2():
    for i in l2:
        p = len(str(abs(i)))
        l21.append(p)
max2()

b = max(l21)

def find():    
    for ele in l2:
        if len(str(abs(ele))) == b:
            print(ele)

find()

def find2():    
    for ele in l2:
        if len(str(abs(ele))) == max(l21)-1:
            print(ele)

find2()