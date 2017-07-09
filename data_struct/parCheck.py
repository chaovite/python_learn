# check the parenthesis

def parCheckSimple(strs_in):
    stack = []
    balanced = True
    for s in strs_in:
        if s=='(':
            stack.append(s)
        elif s==')':
            if len(stack) == 0:
                balanced = False
                break
            else:
                stack.pop()
        else:
            pass
    balanced = len(stack)==0 and balanced
    if balanced:
        print('%10s is balanced'%strs_in)
    else:
        print('%10s is unbalanced'%strs_in)
    return balanced

def parCheckGeneral(strs_in):
    stack = []
    balanced = True
    for s in strs_in:
        if s in '([{':
            stack.append(s)
        elif s in ']})':
            if len(stack) == 0 and not matches(s, stack[-1]):
                balanced = False
                break
            else:
                stack.pop()
        else:
            pass
    balanced = len(stack)==0 and balanced
    if balanced:
        print('%10s is balanced'%strs_in)
    else:
        print('%10s is unbalanced'%strs_in)
    return balanced



def matches(a, b):
    match = (  (a=='(' and b==')') 
            or (a=='{' and b=='}') 
            or (a=='[' and b==']')
            )
    return match


parCheckSimple('()')
parCheckSimple('(a)')
parCheckSimple('jlsd()')
parCheckSimple('((((((')
parCheckSimple("(jlksdj)")
parCheckSimple("(())")

parCheckGeneral('{{([][])}()}')
parCheckGeneral('[{()]')
