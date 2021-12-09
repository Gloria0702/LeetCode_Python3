class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        while len(s) > 0:
            checked = set()
            letter = s[0]
            checked.add(letter)
            last_occurence = s.rfind(letter)
            partition_end = last_occurence
            i = 0
            while i < partition_end:
                if s[i] not in checked:
                    partition_end = max(partition_end, s.rfind(s[i]))
                    checked.add(s[i])
                i += 1
            result.append(partition_end+1)
            s = s[partition_end+1:]
        return result