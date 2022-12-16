def solution(arr):
    arr.sort()
    answer = arr[0]
    for i in range(0, len(arr)-1):
        answer = lcm(answer, arr[i+1])
    return answer

def lcm(a, b):
    A, B = a, b
    while b > 0:
        a, b = b, a % b
    return A * B // a