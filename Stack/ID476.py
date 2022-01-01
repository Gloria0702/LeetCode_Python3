def findComplement(self, decNumber: int) -> int:
    outnum = 0
    index = 0

    while decNumber > 0:
        rem = 1 - (decNumber % 2)
        decNumber = decNumber // 2
        outnum += rem * (2 ** index)
        index += 1

    return outnum