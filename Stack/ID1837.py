def sumBase(decNumber,base):
    remstack = 0

    while decNumber > 0:
        rem = decNumber % base
        remstack += rem
        decNumber = decNumber // base

    return remstack