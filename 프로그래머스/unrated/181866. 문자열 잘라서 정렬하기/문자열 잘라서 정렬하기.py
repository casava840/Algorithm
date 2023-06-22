def solution(myString):
    l = myString.split('x')
    l.sort()
    for i in range(len(l)):
        if len(l[i]) > 0:
            l = l[i:]
            break
    return l