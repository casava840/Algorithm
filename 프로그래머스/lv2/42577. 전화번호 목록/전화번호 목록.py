from collections import deque

def solution(phone_book):
    phone_book.sort()
    que = deque(phone_book)
    answer = True
    while que:
        if que[1].startswith(que[0]):
            return False
        que.popleft()
        if len(que) == 1:
            break
    return answer