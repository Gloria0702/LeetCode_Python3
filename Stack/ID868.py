def binaryGap(n):
        if n < 3:
            return 0
        remstack = []
        while n > 0:
            rem = n % 2
            remstack.append(rem)
            n = n // 2
        gap = []
        gapi = 0
        ini = remstack.pop()
        while remstack != []:
            a = remstack.pop()
            if a == 0:
                gapi += 1
            else:
                gapi += 1
                gap.append(gapi)
                gapi = 0

        if gap == []:
            return 0
        else:
            return max(gap)