# this program demonstrate using stack to convert infix expressions to 
# prefix and postfix

def infixToPostfix(infix_expr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack   = []
    postfixList = []
    tokenList = infix_expr.split()
    for token in tokenList:
        if token=='(':
            opStack.append(token)
        elif token==')':
            while len(opStack)>0 and opStack[-1] != '(':
                postfixList.append(opStack.pop())
            opStack.pop() # pop the '('

        elif token in '+-*/':
            while len(opStack)>0 and prec[opStack[-1]] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.append(token)
        else:
            # operand
            postfixList.append(token)

    # check the opStack.
    while len(opStack)>0:
        postfixList.append(opStack.pop())
    return ' '.join(postfixList)

print(infixToPostfix("( A + B ) * ( C + D ) "))
print(infixToPostfix("( A + B ) * C"))




