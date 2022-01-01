def evalRPN(tokens):
    operandStack = []

    for token in tokens:
        if token not in "+-*/":
            operandStack.append(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.append(result)

    result = operandStack.pop()
    return round(result)


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return int(op1 / op2)
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))