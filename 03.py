# Функция сложения длинных чисел
def summLong(a, b):
    # Создаём копию списка "a" в переменную acopy для того чтобы не изменить оригинал
    acopy = a.copy()

    #  Создаём список "c", в котором будет результат
    c = []

    # До предпоследнего элемента: чтобы не было выхода за границы списка в случае переноса 1 в предпоследнем разряде
    for i in range(len(acopy) - 1):
        summa = acopy[i] + b[i]
        if summa >= 10:
            acopy[i + 1] += 1
            summa -= 10
        c.append(summa)
    return c



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
            print(a[i], end="")
        print()

a = [9, 8, 7, 0, 0]
b = [5, 5, 5, 0, 0]
c = summLong(a, b)

printData(a)
printData(b)
printData(c)
