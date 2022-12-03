l = [1,2,3,4,5,6,7,8,9]

print('#1')
def rev1():
    l1 = l.copy()
    a = list(reversed(l1))
    print(a)
rev1()

print('#2')
def rev2():
    l2 = l.copy()
    l2.reverse()
    print(l2)
rev2()

