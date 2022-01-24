MAX = 100
TOP = -1
stack = []


def push(item):
    global TOP
    if len(stack) >= MAX:
        print('stack overflow')
        return -1
    TOP = TOP + 1
    stack.append(item)
    return stack[TOP]


def pop():
    global TOP
    if TOP == -1:
        print('stack underflow')
        return -1
    element = stack[TOP]
    TOP = TOP - 1
    return element


def print_stack():
    if TOP == -1:
        print('stack is Empty !')
        return
    for j in range(TOP + 1):
        print(stack[j])


for i in range(MAX):
    push(i)

print_stack()
