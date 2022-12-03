l = [12, -7, 5, 64, -14]

def p1():
    p = []
    for p11 in l:
        if p11 == abs(p11):
            p.append(p11)
    print(p)
p1()


def p2():
    for p222 in l:
        if p222 > 0:
            print (p222, end=" ")
p2()

print(end='\n')
print('#', l )
print(max(l))
print(min(l))

def p3():
    for i in range (0, len(l)):
        for n in range(0, max(l)+1):
            if n == l[i]:
                print(n, end = " ") 
p3()

