def solution(today, terms, privacies):
    answer = []
    dic = {}
    present = today[0:4] + today[5:7] + today[8:10]
    for term in terms:
        dic[term[0]] = int(term[2:])
    for i in range(len(privacies)):
        year_int = int(privacies[i][0:4])
        month_int = int(privacies[i][5:7])
        day_str = privacies[i][8:10]
        month_str = ''
        year_plus = dic[privacies[i][-1]]//12
        month_plus = dic[privacies[i][-1]]%12
        
        year_int += year_plus
        month_int += month_plus
        if month_int > 12:
            year_int += 1
            month_int -= 12
        if month_int < 10:
            month_str = '0'+ str(month_int)
        else:
            month_str = str(month_int)
        due_date = str(year_int) + month_str + day_str
        if present >= due_date:
            answer.append(i+1)
    return answer