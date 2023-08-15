def solution(numbers):
    #반복문이 중첩될 것 같을땐 큰 하나의 싸이클이 돌리고 최대한 자잘한 반복은 없도록 처리해야한다.
    length = len(numbers)
    result = [-1] * length

    stack = []
    for i in range(length):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        stack.append(i)
    
    return result