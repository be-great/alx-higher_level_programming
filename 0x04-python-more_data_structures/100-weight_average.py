#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = sum(sore * weight for sore, weight in my_list)
    total_weight = sum(weigth for score, weigth in my_list)

    return total_score / total_weight
