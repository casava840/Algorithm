def solution(clothes):
    answer = 1
    idx = []
    count = []
    clothes.sort(key = lambda x: x[1])
    if len(clothes) == 1:
        return 1
    else:
        for i in range(len(clothes)-1):
            if clothes[i][1] != clothes[i+1][1]:
                idx.append(i)
    if len(idx) == 0:
        return len(clothes)
    count.append(idx[0] +1 +1)
    if len(idx)>1:
        for i in range(1, len(idx)):
            count.append(idx[i]-idx[i-1]+1)
    count.append(len(clothes)-1 - idx[-1] +1)
    for i in count:
        answer *= i
    return answer-1