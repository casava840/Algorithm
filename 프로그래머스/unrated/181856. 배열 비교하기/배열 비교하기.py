def solution(arr1, arr2):
    length1 = len(arr1)
    length2 = len(arr2)
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    if length1 == length2:
        if sum1 == sum2:
            return 0
        elif sum1 > sum2:
            return 1
        else:
            return -1
    if length1 > length2:
        return 1
    return -1
        
    answer = 0
    return answer