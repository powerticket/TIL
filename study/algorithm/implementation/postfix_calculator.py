TOKEN = ['(', '+', '-', '*', '/', ')']
ISP = [0, 1, 1, 2, 2]
ICP = [3, 1, 1, 2, 2]
def postfix_converter(tokens):
    stack = []
    result = []
    for token in tokens:
        if token in TOKEN:
            if stack:
                if token == ')':
                    while stack[-1] != '(':
                        result.append(stack.pop())
                    stack.pop()
                elif ISP[TOKEN.index(stack[-1])] < ICP[TOKEN.index(token)]:
                    stack.append(token)
                else:
                    while ISP[TOKEN.index(stack[-1])] >= ICP[TOKEN.index(token)]:
                        result.append(stack.pop())
                    stack.append(token)
            else:
                stack.append(token)
        else:
            result.append(token)
    while stack:
        result.append(stack.pop())
    return result


def postfix_calculator(tokens):
    stack = []
    for token in tokens:
        if token not in TOKEN:
            stack.append(int(token))
        else:
            b = stack.pop()
            f = stack.pop()
            if token == '+':
                stack.append(f+b)
            elif token == '-':
                stack.append(f-b)
            elif token == '*':
                stack.append(f*b)
            elif token == '/':
                stack.append(f/b)
    return stack.pop()


print(postfix_calculator(postfix_converter('(6+5*(2-8)/2)')))
print(eval('6+5*(2-8)/2'))