def candy(ratings) :
        l = len(ratings)
        num = [1]

        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                num.append(num[i-1]+1)
            else:
                num.append(1)
        for i in range(l-1, 0, -1):
            if (ratings[i] < ratings[i - 1]) and (num[i] >= num[i - 1]):
                num[i - 1] = num[i] + 1
        return sum(num)
print(candy([1,0,2]))