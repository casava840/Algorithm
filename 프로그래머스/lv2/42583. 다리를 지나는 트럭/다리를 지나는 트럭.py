from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    deq = deque(truck_weights)
    bridge_time = deque()
    bridge_weight = deque()
    while deq:
        answer += 1
        if len(bridge_time) != 0 and (answer - bridge_time[0]) == bridge_length:
            bridge_time.popleft()
            bridge_weight.popleft()
        if sum(bridge_weight) + deq[0] <= weight and len(bridge_time) < bridge_length:
            bridge_time.append(answer)
            bridge_weight.append(deq.popleft())
    answer += bridge_length
    
    return answer