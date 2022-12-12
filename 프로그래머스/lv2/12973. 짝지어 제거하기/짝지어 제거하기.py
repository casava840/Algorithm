def solution(s):
    stack = []
    for i in range(len(s)):
        if stack == []:
            stack.append(s[i])          # stack이 비어있다면 push()
        else:
            if s[i] == stack[-1]:       # stack 마지막 값과 s[i]가 같다면 pop()
                stack.pop()
            else:
                stack.append(s[i])
    if stack == []:
        return 1
    else:
        return 0