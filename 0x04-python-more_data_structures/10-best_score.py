#!/usr/bin/python
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    keys = list(a_dictionary.keys())
    score = 0
    for key in keys:
        if a_dictionary[key] > score:
            best = key
            score = a_dictionary[key]
    return best
