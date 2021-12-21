'''To avoid having to sort the dictionary (D), we can just keep track of our best answer (ans), and skip any words that would be a worse answer than the current one.

Then, we can simply check each word to see if we can find the char's in S in order to make the word. We can use a string indexing function to good effect here, making sure to start each new char search from just after the position (pos) of the last char found.

If we fail to find a char, break to the next word. If we successfully reach the end of a word, we can return it. If we never find a valid word match, return an empty string.
'''


def findLongestWord(S, D):
    ans = ""
    for word in D:
        a, b = len(word), len(ans)
        if a < b or (a == b and word > ans): continue
        pos = -1
        for char in word:
            pos = S.find(char, pos + 1)
            if pos == -1: break
        else:
            ans = word
    return ans

print(findLongestWord("abpcplea",
["ale","apple","ee","monkey","plea"]))

class Solution:
    def findLongestWord(self, S: str, D: List[str]) -> str:
        ans = ""
        for word in D:
            a, b = len(word), len(ans)
            if a < b or (a == b and word > ans): continue
            pos = -1
            for char in word:
                pos = S.find(char, pos + 1)
                if pos == -1: break
            else: ans = word
        return ans


# class Solution:
#     def findLongestWord(self, s: str, dictionary: List[str]) -> str:
#         # Sort the dictionary by length and then lexographical order
#         dictionary.sort(key=lambda x: (-len(x), x))
#
#         for d in dictionary:
#             count = 0
#             i = j = 0
#             while j < len(d) and i < len(s):
#                 # Start counting whenever a character matches
#                 if s[i] == d[j]:
#                     j += 1
#                     count += 1
#                 i += 1
#             # return as soon as you find all the characters from dictionary word in s
#             if count == len(d):
#                 return d
#
#         return ''


# class Solution:
#     def findLongestWord(self, s: str, dictionary: List[str]) -> str:
#
#         # dictionary.sort(key= lambda x: (-len(x),x))
#
#         ans = ''
#
#         for d in dictionary:
#             count = 0
#             i = j = 0
#             while j < len(d) and i < len(s):
#                 if s[i] == d[j]:
#                     j += 1
#                     count += 1
#                 i += 1
#             if count == len(d):
#                 if len(d) > len(ans):
#                     ans = d
#                 if len(d) == len(ans) and d < ans:
#                     ans = d
#
#         return ans