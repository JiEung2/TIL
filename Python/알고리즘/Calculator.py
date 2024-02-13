# top = -1
# stack = [0] * 100
#
# icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
#
# fx = '(6+5*(2-8)/2)'
# postfix = ''
#
# for tk in fx:
#     # 여는 괄호 push, 연산자이고 top 원소보다 우선순위가 높으면 push
#     if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
#         top += 1
#         stack[top] = tk
#     elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:   # 연산자이고 top 원소보다 우선순위가 높지 않으면
#         while isp[stack[top]] >= icp[tk]:   # top원소의 우선순위가 낮을 때까지 pop
#             postfix += stack[top]
#             top -= 1
#         top += 1
#         stack[top] = tk
#     elif tk == ')':     # 닫는 괄호면, 여는 괄호를 만날때까지 pop
#         while stack[top]!='(':
#             postfix += stack[top]
#             top -= 1
#         top -= 1
#         stack[top + 1]
#     else:
#         postfix += tk
#

# # s = '(6+5*(2-8)/2'
# s = '2+3*4/5'
#
# stack = []
# result = []
#
# prio = {'+': 1, '*': 2, '-': 1, '/': 2}
# for c in s:
#     if c.isdigit():
#         result.append(c)
#     else:
#         if stack and prio[stack[-1]] < prio[c]:
#             stack.append(c)
#         else:
#             while stack and prio[stack[-1]] >= prio[c]:
#                 result.append(stack.pop())
#             stack.append(c)
# while stack:
#     result.append(stack.pop())
#
# print(result)

# s = '(6+5*(2-8)/2)'
# # s = '2+3*4/5'
#
# stack = []
# result = []
# icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
#
# for c in s:
#     if c.isdigit():
#         result.append(c)
#     elif c == ')':
#         while stack[-1] != '(':
#             result.append(stack.pop())
#         stack.pop()
#     else:
#         if stack and isp[stack[-1]] < icp[c]:
#             stack.append(c)
#         else:
#             while stack and isp[stack[-1]] >= icp[c]:
#                 result.append(stack.pop())
#             stack.append(c)
# while stack:
#     result.append(stack.pop())
#
# print(result)


s = '(6+5*(2-8)/2)'
# s = '2+3*4/5'
# prio = {'+':1, '*':2, '-':1, '/':2, '(':100}
icp = {'+': 1, '*': 2, '-': 1, '/': 2, '(': 100}
isp = {'+': 1, '*': 2, '-': 1, '/': 2, '(': 0}


def step1():
    ST = []
    result = []
    for c in s:
        if c.isdigit():
            result.append(c)
        elif c == ')':
            while ST[-1] != '(':
                result.append(ST.pop())
            ST.pop()
        else:
            if ST and isp[ST[-1]] < icp[c]:
                ST.append(c)
            else:
                while ST and isp[ST[-1]] >= icp[c]:
                    result.append(ST.pop())
                ST.append(c)

    while ST:
        result.append(ST.pop())
    return result


def step2(lst):
    ST = []
    for c in lst:
        if c.isdigit():
            ST.append(c)
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            # t = calc(v1,v2,c)
            ST.append(calc(int(v1), int(v2), c))
    return ST.pop()


def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    else:
        return v1 // v2


post_order = step1()
print(step2(post_order))