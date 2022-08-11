def fibonacci(n, a = 1, b = 1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n - 1, b, a + b)

def vsota_sodih():
    vsota = 0
    i = 0
    while fibonacci(i) <= 4000000:
        if fibonacci(i) % 2 == 0:
            vsota += fibonacci(i)
        i += 1
    return vsota
 
print(vsota_sodih())
