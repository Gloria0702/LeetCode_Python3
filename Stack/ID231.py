def isPowerOfTwo(n):
    que = []
    if n == 1:
        return True
    while n > 0:
        res = n % 2
        que.append(res)
        n = n // 2
    if que != []:
        s = que.pop()
        if (s == 1) and (1 not in que):
            return True
        else:
            return False
    else:
        return False