def solution(n):
    binary = bin(n)
    if '01' in binary:
        index1 = binary.rfind('01')
        count = binary.count('1',index1+2)
        new_binary = binary[:index1] + '10' + '0'*(len(binary)-index1-2-count) + '1'*count
    else:
        count = binary.count('1', 3)
        new_binary = binary[:3] + '0' + '0'*(len(binary)-3-count) + '1'*count
    return int(new_binary,2)