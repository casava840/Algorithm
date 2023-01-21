from itertools import permutations

def solution(k, dungeons):
    dun_size = len(dungeons)
    answer = 0
    for permutation in permutations(dungeons,dun_size):
        pirodo = k
        count = 0
        for case in permutation:
            if case[0] <= pirodo:
                pirodo -= case[1]
                if pirodo < 0:
                    break
                count += 1
            else:
                break
            if count > answer:
                answer = count
    return answer