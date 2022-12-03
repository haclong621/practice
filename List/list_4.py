list = test_list = [1, 6, 3, 5, 3, 4]
i = int(input('nhap vao: '))
m = any([0,0,1])
print(m)


def check():
    a = list.count(i)
    if a > 0:
        print("Check 1: True")
    else: print("Check 1: False")
check()

def check2():
    for b in list:
        if i == b :
            print ('1')
        else:
            print('0')
check2()