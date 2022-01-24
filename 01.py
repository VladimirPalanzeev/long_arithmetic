# Функция преобразования списка в число
def getData(a):
    d = 0
    length = len(a)

    for i in range(length):
        d += a[i] * 10 ** i
    return d

def printData(a):
    for i in range(len(a) - 1, -1, -1):
        print(f"{a[i]}", end="")
    print()


a = [3, 2, 1]
print(getData(a))

b = [54, 21, 67, 12, 54]
print(getData(b))

b = [4, 6, 9, 8, 5, 5]
print(getData(b))

print("Обычное число")
a = [4, 6, 9, 8, 5, 5]
printData(a)
print(getData(a))
print("\nЗашифрованное число")
c = [54, 21, 67, 12, 54]
printData(c)
print(getData(c))

