# Функция преобразования списка в число
def getData(a):
    d = 0
    length = len(a)

    for i in range(length):
        d += a[i] * 10 ** i
    return d

a = [3, 2, 1]
print(getData(a))