l = [15, 9, 55, 41, 35, 20, 62, 49]
print('for: 0-', len(l))
i = int(input('Choice: '))

def s1():
    print(sum(l) ,' ', sum(l)/len(l))
s1()


def s2():
    print (sum(l[0:i]) / len(l[0:i]))
s2()