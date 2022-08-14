def kvadrat_vsote(n):
    return sum(range(1, n + 1)) ** 2

def vsota_kvadratov(n):
    return sum([i ** 2 for i in range(1, n + 1)])

print(kvadrat_vsote(100) - vsota_kvadratov(100))