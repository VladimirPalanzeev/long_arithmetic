
# Функция перевода йз 10-чной в систему счисления X
def toBase(x, base):
    # Список с возвращаемым результатом
    ret = []

    # Пока X не "исчерпает себя"
    while x > 0:
        # Добавляем остаток от деления в возвращаемый список
        ret.append(x % base)
        # Уменьшаем x
        x //= base

    # Добавляем два дополнительных разряда в конец списка для того,
    # чтобы при суммировании не было ошибок и возвращаем список
    ret.append(0)
    ret.append(0)
    return ret


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

a = toBase(75, 2)
printData(a)

a = toBase(176, 16)
printData(a)

print()