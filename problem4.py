def je_palindrom(n):
    niz = str(n)
    return niz == niz[::-1]

def najvecji_palindrom():
    najvecji = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if je_palindrom(i * j) and i * j > najvecji:
                najvecji = i * j
    return najvecji

print(najvecji_palindrom())

