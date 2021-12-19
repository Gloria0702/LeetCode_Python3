def twoSum(numbers, target):
        l = 0
        r = len(numbers) - 1
        while (l<r):
            sum = numbers[l] +numbers[r]
            if sum == target:
                break
            if sum < target:
                l+= 1
            else:
                r -=1
        return [l+1,r+1]