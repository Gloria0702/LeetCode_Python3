
def findContentChildren( g, s):
        num = 0
        a = min(len(g), len(s))
        g.sort()
        s.sort()
        while num < a and min(len(g), len(s))>0:
            if s[0] < g[0]:
                del s[0]

            else:
                num += 1
                del s[0]
                del g[0]
        return num

# print(findContentChildren([1,2,3], [1,1]))
# print(findContentChildren([1,2,3], [2,3]))
print(findContentChildren([3,4], [1,3,4]))