import math

def solution(fees, records):
    answer = []
    park = {}
    for record in records:
        car_num = record[6:10]
        if record.endswith('IN'):
            if car_num in park:
                park[car_num] += 1439 - int(record[0:2]) * 60 - int(record[3:5])
            else:
                park[car_num] = 1439 - int(record[0:2]) * 60 - int(record[3:5])
        else:
            park[car_num] -= 1439 - int(record[0:2]) * 60 - int(record[3:5])
    park_sorted = dict(sorted(park.items()))
    for car_num in park_sorted:
        if park_sorted[car_num] <= fees[0]:
            cost = fees[1]
        else:
            cost = math.ceil((park_sorted[car_num] - fees[0]) / fees[2]) * fees[3] + fees[1]
        answer.append(cost)
        
    return answer