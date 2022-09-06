def najvecja_vsota():
    vsote = []
    for a in range(1,100):
        for b in range(1, 100):
            stevilo = a ** b
            vsota = 0
            for n in str(stevilo):
                vsota += int(n)
            vsote.append(vsota)
    return max(vsote)

print(najvecja_vsota())