# 在公司已开发一半的功能，在家写了其他功能
a = list()
b = list()
for i in range(10):
    a.append(i)
    b.append(a[i+1])

print(a)
print(b)