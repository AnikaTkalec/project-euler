def pitagorejski_trojcek(a, b):
    from math import sqrt
    c = sqrt(a ** 2 + b ** 2)
    return c

def produkt():
    for a in range(1,500):
        for b in range(1,500):
            c = pitagorejski_trojcek(a, b)
            if a + b + c == 1000:
                return a * b * c
                
print(produkt())