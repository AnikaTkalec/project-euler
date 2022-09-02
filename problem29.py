def stevilo_clenov():
    sez = []
    for a in range(2,101):
        for b in range(2,101):
            if a ** b not in sez:
                sez.append(a ** b)
    return len(sez)

print(stevilo_clenov())
