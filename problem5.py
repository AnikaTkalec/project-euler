from re import I


def enakomerno_deljivo():
    i = 1
    while True:
        for m in range(2,21):
            if i % m != 0:
                break
        else:
            break
        i += 1
    return i 

print(enakomerno_deljivo())
