def resitev():
    vsota = 0
    for i in range(1, 1001):
        vsota += i ** i
    return str(vsota)[-10:]

print(resitev())