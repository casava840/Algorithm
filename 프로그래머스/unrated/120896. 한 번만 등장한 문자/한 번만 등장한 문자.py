from collections import Counter
def solution(s):
    c = Counter(s)
    picked = [char for char, count in c.items() if count == 1]
    picked.sort()

    return ''.join(picked)