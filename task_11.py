a = [2, 4, 5, 6, 7, 10, 11]

b = len(a)

print(b)

i = 0

count = 0

while i < b:
    if a[i] % 2 == 0:
        count += 1
    i += 1
print(count)
