def solution(people, limit):
    people.sort()
    count = 0
    light_idx = 0
    heavy_idx = len(people)-1
    while light_idx<heavy_idx:
        if people[light_idx] + people[heavy_idx] <= limit:
            count += 1
            light_idx += 1
            heavy_idx -= 1
        else:
            heavy_idx-=1
    answer = len(people)-count
    return answer