def vsota_stevk(n):
    if n == 0:
        return 0
    else:
        return vsota_stevk(n // 10) + n % 10 