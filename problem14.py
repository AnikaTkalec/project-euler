
def dolzina_collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + dolzina_collatz(n // 2)
    return 1 + dolzina_collatz(3 * n + 1)

print(dolzina_collatz(13))

def najdaljsi_collatz():
    najdaljsi = 0
    najboljsi = 1
    for n in range(1, 1000000):
        rezultat = dolzina_collatz(n)
        if najdaljsi < rezultat:
            najdaljsi = rezultat
            najboljsi = n
    return najboljsi

print(najdaljsi_collatz())