from collections import Counter

def solution(participant, completion):
    cp = Counter(participant)
    cc = Counter(completion)
    
    spare = cp - cc
    return list(spare.elements())[0]