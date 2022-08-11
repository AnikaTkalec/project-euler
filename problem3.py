def najvecji_prafaktor(n):
    i = 2
    while i < n:
        while n % i == 0:
            n = n / i
        i += 1
    return i

print(najvecji_prafaktor(600851475143))