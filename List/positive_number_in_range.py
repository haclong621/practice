st = int(input("Bat dau: ", ))
en = int(input("Ket thuc: ", ))

print('So duong la: ')
for i in range(st, en+1):
    if i > 0:
        
        print (i, end = ' ')

print(end = '\n')
print('So am la: ')
for j in range(st, en+1):
    if j < 0:
        
        print (j, end = ' ')