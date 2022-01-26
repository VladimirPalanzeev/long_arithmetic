def getData(a, base):
    d = 0
    length = len(a)

    for i in range(length):
        d += a[i] * base ** i
    return d
a = [3, 2, 1]
print(getData(a, 16))

a = [0, 0, 0, 0, 1]
print(getData(a, 16))