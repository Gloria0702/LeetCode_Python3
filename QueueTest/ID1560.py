class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        if rounds[0] == rounds[-1]:
            return [rounds[0]]

        arr = []

        if rounds[0] < rounds[-1]:
            for i in range(rounds[0], rounds[-1] + 1):
                arr.append(i)

        else:
            for i in range(rounds[0], rounds[-1] + n + 1):
                if i == n:
                    arr.append(n)
                else:
                    arr.append(i % n)

        return sorted(arr)