from math import sqrt
def je_prastevilo(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def vsota_prastevil(n):
    i = 2
    vsota = 0
    a = je_prastevilo(i)
    for i in range(2, n):
        if je_prastevilo(i):
            vsota += i
        else:
            vsota = vsota
    return vsota

print(vsota_prastevil(2000000))


