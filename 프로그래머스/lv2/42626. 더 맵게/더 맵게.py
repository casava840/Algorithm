from heapq import *

def solution(scoville, K):
    count = 0
    heapify(scoville)
    while True:
        if scoville[0] >= K or len(scoville) == 1:
            break
        new = heappop(scoville) + heappop(scoville) * 2
        heappush(scoville, new)
        count += 1
    if scoville[0] >= K:
        return count
    else:
        return -1