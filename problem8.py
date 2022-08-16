def preberi_tekst():
    with open('input8.txt', 'r') as datoteka:
        rezultat = ''
        for vrstica in datoteka:
            rezultat += vrstica.strip()
        return rezultat


def resitev():
    tekst = preberi_tekst()
    najvecji_produkt = 0
    for i in range(len(tekst) - 13):
        trenutni = 1
        for j in range(13):
            trenutni *= int(tekst[i + j])
        if trenutni > najvecji_produkt:
            najvecji_produkt = trenutni
    return najvecji_produkt

print(resitev())