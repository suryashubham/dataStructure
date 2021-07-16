def check_balance(expression):
    left_parenthesis = ['(', '{', '[']
    stack = []
    for bracket in expression:
        if bracket in left_parenthesis:
            stack.append(bracket)
        else:
            popped_bracket = stack.pop(-1)
            if (bracket == ')' and popped_bracket == '(') or (bracket == '}' and popped_bracket == '{') or (
                    bracket == ']' and popped_bracket == '['):
                continue
            else:
                return -1
    if len(stack) > 0:
        return -1
    return 'balanced'


print(check_balance('{([]){}[]}{{{'))
