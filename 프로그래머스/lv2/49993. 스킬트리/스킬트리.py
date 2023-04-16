def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        temp = ""
        for i in range(len(s)):
            if s[i] in skill:
                temp += s[i]
        if len(temp) == 0:
            answer += 1
        elif temp[0] == skill[0] and temp in skill:
            answer += 1
    return answer