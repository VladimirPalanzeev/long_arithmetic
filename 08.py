from random import randint

# Выводим список на экран
def printData(a):
    # p - маркер номера позиции, в которой в списке находится "не ноль"
    # Задаём индекс последнего элемента
    p = len(a) - 1

    # Пока первый встреченный с конца элемент равен 0, уменьшаем p
    while a[p] == 0 and p >= 0:
        p -= 1
    if p == -1:
        print(0)
    else:
        # Перебираем значения и выводим на экран
        for i in range(p, -1, -1):
            print(alphabet[a[i]], end="")
        print()

# Функция сложения длинных чисел
def summLong(a, b, base):
    # Создаём копию списка "a" в переменную acopy для того чтобы не изменить оригинал
    acopy = a.copy()

    #  Создаём список "c", в котором будет результат
    c = []

    # До предпоследнего элемента: чтобы не было выхода за границы списка в случае переноса 1 в предпоследнем разряде
    for i in range(len(acopy) - 1):
        summa = acopy[i] + b[i]
        if summa >= base:
            acopy[i + 1] += 1
            summa -= base
        c.append(summa)
    return c
# Переводим число из системы с основанием base в десятичную
def getData(a, base):
    d = 0
    length = len(a)
    for i in range(length):
        d += a[i] * base ** i
    return d

# Всего 128 символов
alphabet = "0123456789"
alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += "abcdefghijklmnopqestuvwxyz"
alphabet += "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet += "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

n = 5
base = 100

# Заполняем списки случайными числами от 0 до base
# (в системе счисления не может быть знака больше или равного основанию)
a = [randint(0, base - 1) for i in range(n)]
b = [randint(0, base - 1) for i in range(n)]

# Добавляем "запасные" ячейки, чтобы при сложении не выйти за границы списка
a.append(0)
a.append(0)
b.append(0)
b.append(0)

c = summLong(a, b, base)
print("Первое число:")
printData(a)
print(f"В десятичной системе: {getData(a, base)}")
print("\nВторое число:")
printData(b)
print(f"В десятичной системе: {getData(b, base)}")
print("\nСумма:")
printData(c)
print(f"В десятичной системе: {getData(c, base)}")
