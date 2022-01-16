matrix = []
n = int(input('Введите количество строк '))
m = int(input('Введите количество столбцов '))

for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input('Введите элемент ')))
    matrix.append(a)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

b = []
for i in range(n):
    sum = 0
    for j in range(m):
        sum+=matrix[i][j]
    b.append(sum)
    print(f'Сумма {i} строки = {sum}')

max1 = max(b)
ind_max=b.index(max1)
print(f'номер строки, сумма чисел в которой максимальна равна {ind_max}')