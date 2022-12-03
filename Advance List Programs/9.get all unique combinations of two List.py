l1 = ["a", "b", "c","d"]
l2 = [1,4,9]
#Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] 

def g1():
    res = []
    for a in l1:
        for b in l2:
            res. append([a,b])
    print(res)
g1()

def g2():
    res = []
    for b in l2:
        for a in l1:
            res. append([a, b])
    print(res)
g2()

def g3():
    from itertools import permutations
    a =  list(permutations(l1))
    b = list(permutations(l2))
    
    for a1 in a:
        for b1 in b:
            print(list(zip(a1,b1)))

g3()


def g4():
    from itertools import permutations
    res = []
    g44 = list(permutations(l1, len(l2)))
    for a in g44:
        res.append(list(zip(a,l2)))
    print(res)
g4()
