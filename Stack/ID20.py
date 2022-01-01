class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Solution:
    def isValid(self, s: str) -> bool:
        sa = Stack()
        balanced = True
        index = 0
        while index < len(s) and balanced:
            symbol = s[index]
            if symbol in "([{":
                sa.push(symbol)
            else:
                if sa.isEmpty():
                    return False
                top = sa.pop()
                if not matches(top, symbol):
                    balanced = False
            index += 1
        if balanced and sa.isEmpty():
            return True
        else:
            return False


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)