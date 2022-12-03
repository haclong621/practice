l  = [[4, 1, 6], [7, 8], [4, 10, 8]]
#[[6, 4, 1], [8, 7], [10, 8, 4]]


def f1():
    l1 = l.copy()
    l11 = []
    for i in l:
        sort = sorted(i)
        rev = list(reversed(sort))
        nl = list(rev)
        l11.append(nl)
    print('#1: ', l11)
    
    for i in l1:
        l2 = (map(lambda i : list(reversed(sorted(i))) , l))
    print('#2: ', list(l2))
 
    
f1()
