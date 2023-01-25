def solution(elements):
    LENGTH = len(elements)
    circle = elements * 2
    case = 1
    sum_list = []
    while case != LENGTH+1:
        for i in range(LENGTH):
            sum_list.append(sum(circle[i:i+case]))
        case += 1
    return len(set(sum_list))