def bitwiseComplement(n):
    if n == 0:
        return 1
    com = 0
    index = 0
    while n > 0:
        com += (1-(n % 2)) * (2**index)
        index += 1
        n = n // 2

    return com

