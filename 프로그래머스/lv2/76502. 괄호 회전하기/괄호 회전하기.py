def solution(s):
    if len(s) <2:
        return 0
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if check(s):
            answer += 1
    return answer

def check(s):
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        elif char == ')' and stack[-1] == '(':
            stack.pop()
        elif char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == ']' and stack[-1]  == '[':
            stack.pop()
        else:
            stack.append(char)
    if len(stack) == 0:
        return True
    else:
        return False