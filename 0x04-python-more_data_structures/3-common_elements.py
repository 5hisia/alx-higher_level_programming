#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for common in set_1:
        if common in set_2:
            result.append(common)
    return result
