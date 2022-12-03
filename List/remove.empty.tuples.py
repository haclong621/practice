tup = [(), ('ram' , '15' , '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]



def rem1():
    tup1 = tup.copy()
    for i in tup1:
        if i == ():
            tup1.remove(i)
    print(tup1)
rem1()


def r2():
    r22 = filter(None, tup)
    print(list(r22))
r2()
    
    
def r3():
    r33 = [t for i, t in enumerate(tup) if t]
    print(r33)
r3()

            