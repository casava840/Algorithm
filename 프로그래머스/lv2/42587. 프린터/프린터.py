from collections import deque

def solution(priorities, location):
    que = [(i,p) for i,p in enumerate(priorities)]
    print_que = deque([])
    prior_que = deque(que)
    temp_que = deque([])
    while prior_que:
        if len(print_que) == 0:
            print_que.append(prior_que.popleft())
        elif print_que[-1][1] >= prior_que[0][1]:
            print_que.append(prior_que.popleft())
        else:
            while print_que[-1][1] < prior_que[0][1]:
                temp_que.append(print_que.pop())
                if len(print_que) == 0: break
            print_que.append(prior_que.popleft())
            while temp_que:
                prior_que.append(temp_que.pop())
    for i in range(len(print_que)):
        if print_que[i][0] == location:
            return i+1