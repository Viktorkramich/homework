from random import randint

matrix = []

n = int(input())
m = int(input())
for i in range(n):
    line = []
    for j in range(m):
        line.append(randint(0, 10))
    matrix.append(line)
print(matrix)
list = []
d = 0
for i in matrix:
    c = max(matrix[d])
    list.append(c)
    d += 1
print("максимальный элемент матрицы:", max(list))
h = 0
list2 = []
for i in matrix:
    z = min(matrix[h])
    list2.append(z)
    h += 1
print("минимальный элемент матрицы:", min(list2))

list3 = []
for i in matrix:
    v = sum(i)
    list3.append(v)
print("сумма всех элементов матрицы:",sum(list3))


list4 = []
for i in matrix:
    list4.append(sum(i))
    w = 0
    for j in matrix:

        if sum(j) == max(list4):
            m = str(w)+str(j)
        w += 1


print("индекс максимального ряда -", m)

list5 = []
for i in matrix:
    list5.append(sum(i))
    w = 0
    for j in matrix:

        if sum(j) == min(list5):
            m = str(w)+str(j)
        w += 1


print("индекс минимального ряда -", m)

list6 = []
for i in matrix:
    for j in i:
        list6.append(j)
        print(list6)
