from math import sqrt

def zaporedje_trikotnika(n):
    return sum(range(n + 1))

def deljitelji(n):
    seznam_deljiteljev = {1}
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            seznam_deljiteljev |= {i, n // i}
    seznam_deljiteljev.add(n)
    return seznam_deljiteljev

def prvo_stevilo():
    i = 1
    while len(deljitelji(zaporedje_trikotnika(i))) <= 500:
        i += 1
    return zaporedje_trikotnika(i)

print(prvo_stevilo())