def preberi_tekst():
    with open('input13.txt', 'r') as datoteka:
        vsota = 0
        for vrstica in datoteka:
            vsota += int(vrstica)
        return vsota



def prvih_deset():
    stevilo = preberi_tekst()
    return int(str(stevilo)[:10])

print(prvih_deset())

