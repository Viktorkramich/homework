a = [2, 4, 5, 6, 7, 10, 11]

b = len(a)

i = 0

count = 0

while i < b:
    if a[i] % 2 == 0:
        count += 1
    i += 1
print(count)


ab = [2, 4, 5, 6, 7, 10, 11]

count_1 = 0

for item in ab:
    if item % 2 == 0:
        count_1 += 1
print(count_1)
