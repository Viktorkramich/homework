a = str(input())

b = int(len(a) / 2)

print(a[b])

if a[b] == a[0]:
    c = a[1:-1]
    print(c)
