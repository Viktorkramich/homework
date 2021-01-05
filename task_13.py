my_list = [1,2,3,4,5]

my_list_len = len(my_list)

new_list = []

i = 0

while i <  my_list_len:
    if i + 1 == my_list_len:
        new_list.append(my_list[0])
    else:
        new_list.append(my_list[i + 1])
    i += 1

print(new_list)


a = [1,2,3,4,5]
b = []
c = 1
for i in a:
    if i == a[-1]:
        b.append(a[0])
    else:
        b.append(a[c])
        c += 1
print(b)
