from collections import Counter

def solution(k, tangerine):
    c = Counter(tangerine).most_common()
    i = 0
    sum = 0
    while True:
        sum += c[i][1]
        if sum >= k:
            break
        else:
            i += 1
    return i + 1