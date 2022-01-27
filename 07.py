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


alphabet = "0123456789"
alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += "abcdefghijklmnopqestuvwxyz"
alphabet += "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet += "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

# Вывод на экран числа 2730(10) равного AAA(16)
a = [10, 10, 10, 0, 0]
printData(a)

# Посчитаем сумму чисел BEDA(16) + BABA(16)
a = [10, 13, 14, 11, 0, 0]
b = [10, 11, 10, 11, 0, 0]

c = summLong(a, b, 16)
printData(a)
printData(b)
printData(c)

# Проверим десятичную систему
a = [3, 3, 3, 0, 0, 0]
b = [7, 7, 7, 0, 0, 0]

c = summLong(a, b, 10)
printData(a)
printData(b)
printData(c)