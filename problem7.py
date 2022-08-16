from math import sqrt
def je_prastevilo(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def resitev():
    indeks = 0
    i = 1
    while indeks < 10001:
        if je_prastevilo(i):
            indeks += 1
        i += 1
    return i - 1

print(resitev())

    
