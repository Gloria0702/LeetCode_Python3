#Stack: Last in firt out
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
s = Stack()
s.isEmpty()
s.push(4)
s.push('abc')
s.pop()


from pythonds.basic import Stack
#check whether the brackets are paired
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def parChecker_multi(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        #if symbol == "(" or symbol == "[" or symbol == "{" :
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False

            # elif symbol == ")" and s.peek() =="(":
            #     s.pop()
            # elif symbol == "]" and s.peek() =="[":
            #     s.pop()
            # elif symbol == "}" and s.peek() =="{":
            #     s.pop()
            top = s.pop()
            if not matches(top,symbol):
               balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

#Decimal to Binary
def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return int(binString)

#Convert a decimal number to an arbitrary number
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


#Polish notation and Reverse Polish notation

#Infix notation to Prefix notation("Polish") or Reverse Polish notation
#Infix notation to Reverse Polish notation
import string

def infixtopostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                        postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

        return " ".join(postfixList)

infixtopostfix("( A + B ) * ( C + D )")

#Calculate Reverse Polish notation
def postfixEval(postfitExpr):
    operandStack = Stack()

    tokenList = postfitExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()
def doMath(op,op1,op2):
    if op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1+op2
    else:
        return op1-op2
postfixEval("3 2 *")