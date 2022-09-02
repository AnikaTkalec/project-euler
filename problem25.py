def prvi_clen():
    zap = [1, 1]
    while len(str(zap[-1])) < 1000:
        n = zap[-2] + zap[-1]
        zap.append(n)
    return zap.index(n) + 1

print(prvi_clen())
