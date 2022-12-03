t = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
k = ["name", "id"]
 # [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]

def d1():
    print("#1")
    for t1 in range(0, len(t),2):
        d11 = {k[0]: t[t1]}, {k[1]: t[t1+1]}
        print(d11)
d1()


def d2():
    print('#2')
    d22 = [({k[0]: t[x]}, {k[1]: t[x+1]}) for x in range(0, len(t), 2)]
    for i in d22:
        print(i)
d2()