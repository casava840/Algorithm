from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_arr = []
    str2_arr = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_arr.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_arr.append(str2[i:i+2])
    if len(str1_arr) == 0 and len(str2_arr) == 0:
        return 65536
    elif len(str1_arr) == 0 or len(str2_arr) == 0:
        return 0
    else:
        str1_counter = Counter(str1_arr)
        str2_counter = Counter(str2_arr)

        common = (str1_counter & str2_counter).values()
        common_count = 0
        for i in common:
            common_count += i
        whole = (str1_counter | str2_counter).values()
        whole_count = 0
        for i in whole:
            whole_count += i
        answer = int(common_count / whole_count * 65536)
        return answer