t = ['Gfg', 'is', 'best', 'for', 'Geeks']

l = ",".join(t)
print(l)
m = l.replace('G','-') . replace('e','G') . replace('-','e')
print(m)
n = m.split(",")
print(n)

print('#')
def swap():
    t1 = [sub.replace('G','-') . replace('e','G') . replace('-','e') for sub in t]
    print(t1)
    
swap()