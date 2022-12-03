l1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
l2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

def i1():
    for a in l1:
        for b in l2:
            if a == b:
                print(a, end =" ") 
i1()

def i2():
    i22 = list(filter(lambda a: a in l1,l2))
    print(i22)
i2()