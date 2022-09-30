#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        total_weight = 0
        total_score = 0
        for score, weight in my_list:
            total_score += score*weight
            total_weight += weight
        avg_w = total_score/total_weight
        return avg_w
