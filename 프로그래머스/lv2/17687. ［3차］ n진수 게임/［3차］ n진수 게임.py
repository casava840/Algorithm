import string

def solution(n, t, m, p):
    def convert(num,base):
        temp = string.digits + string.ascii_uppercase
        q, r = divmod(num, base)
        if q == 0:
            return temp[r]
        else:
            return convert(q, base) + temp[r]
    answer = ''
    num = -1
    s = ''
    while(len(s) < t * m):
        num += 1
        s += convert(num, n)
    for i in range(t):
        answer += s[m*i + p-1]
    return answer