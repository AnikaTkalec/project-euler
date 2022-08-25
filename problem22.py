def preberi_tekst():
    with open('p022_names.txt', 'r') as datoteka:
        sez_imen = []
        for ime in datoteka.readline().split(","):
            sez_imen.append(ime.replace('"','').strip())
        return sorted(sez_imen)


import string

def vrednosti_crk(ime):
    vrednost_imena = 0
    for i, crka in enumerate(string.ascii_uppercase, 1):
        if crka in ime:
            vrednost_imena += i * ime.count(crka)
    return vrednost_imena

def resitev():
    seznam = preberi_tekst()
    vsota = 0
    for i, k in enumerate(seznam, 1):
        print(i, vrednosti_crk(k))
        vsota += i * vrednosti_crk(k)
    return vsota

print(resitev())



