import matplotlib.pyplot as plt
import math
def merge_sort(points, key='x'):
    if len(points) <= 1:
        return points

    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]

    left_sorted = merge_sort(left_half, key)
    right_sorted = merge_sort(right_half, key)

    return merge(left_sorted, right_sorted, key)

def merge(left, right, key):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if key == 'x':
            if left[left_index][0] <= right[right_index][0]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        elif key == 'y':
            if left[left_index][1] <= right[right_index][1]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def distance(P1, P2):
    """
    Calculate the distance between two points P1 and P2.
    """
    return math.sqrt((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2)
