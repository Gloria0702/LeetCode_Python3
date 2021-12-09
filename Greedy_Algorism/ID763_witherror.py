def frequency(text):
    dict = {}
    pos_b = {}
    pos_e = {}
    for i,char in enumerate(text):
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
            pos_e[char] = i
        else:
            dict[char] = 1
            pos_e[char] = i
            pos_b[char] = i
    return dict, pos_b, pos_e

def partitionLabels(s):
        dicta, pos_b, pos_e = frequency(s)
        keys = list(dicta.keys())
        l = len(keys)
        i = 0
        ind = 1
        end = 0
        out = []
        end_c = s[len(s)-1]
        while (i <= l-1) and (ind+i <= l-1):

            while pos_e[keys[i]] >= pos_b[keys[i+ind]]:
                # a = keys[i]
                # b = keys[i+ind]
                ind += 1

                if ind+i > l-1:
                    end = 1
                    break
            ind -= 1
            if (end == 0) and (end_c != keys[i+ind]):
                out.append(pos_b[keys[i+ind+1]]-pos_b[keys[i]])
            else:
                out.append(len(s) - pos_b[keys[i]])
                break
            i = i + ind + 1
            ind = 1

        if (len(s) == 1):
            out.append(1)
        if (i == l-1) and (l != 1):
            if (pos_b[keys[i]] == pos_e[keys[i]]):
                out.append(1)
        return out

# dict, pos_b, pos_e = frequency("aba")
# print(partitionLabels("aba"))#3
# print(partitionLabels("a"))#1
# print(partitionLabels("eccbbbbdec"))#10
# print(partitionLabels("ababcbacadefegdehijhklij"))##[9,7,8]
# print(partitionLabels("eaaaabaaec"))##[9,1]
print(partitionLabels("qiejxqfnqceocmy")) ##[13,1,1]
# print(partitionLabels(""))
# print(partitionLabels(""))
# print(partitionLabels(""))