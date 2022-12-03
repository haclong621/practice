list1 = ['a' , 'b', 'c', 'd']
list2 = [1,2,3,4,5]

#1
def copy1():
    L1 = list1.copy()
    print('#1: ',L1)
copy1()

#2
def copy2():
    L2 = list1[::1]
    print('#2: ',L2)
copy2()

print([list1])

#3
def copy3():
    L3 = []
    (L3.extend(list1))
    print('#3: ', L3)
copy3()

#4
def copy4():
    import copy
    L4_shadow = copy.copy(list1)
    L5_deep = copy.deepcopy(list2)
    print('#4-1: ', L4_shadow)
    print('#4-2: ', L5_deep)
copy4()

#5
def copy5():
    L5 = []
    for i in range(len(list1)):
        L5.append(list1[i])
    print('#5: ', L5)
copy5()

#6
def copy6():
    L6 = list(map(lambda a: a, list1))
    print('#6: ', L6)
copy6()
    