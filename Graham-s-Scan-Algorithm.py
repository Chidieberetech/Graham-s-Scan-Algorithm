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

def closest_pair_naive(points):
    """
    Naive algorithm to find the closest pair of points by checking distances pair-by-pair.
    """
    min_distance = float('inf')
    closest_points = ()

    n = len(points)
    for a in range(n):
        for b in range(a + 1, n):
            dist = distance(points[a], points[b])
            if dist < min_distance:
                min_distance = dist
                closest_points = (points[a], points[b])

    return min_distance, closest_points

def closest_pair(points):
    """
    Divide & Conquer algorithm to find the closest pair of points in a given set.
    """
    n = len(points)

    # if there are only two or three points, use brute force.
    if n <= 3:
        return closest_pair_naive(points)

    # Sort points by x-coordinate
    points_sorted_by_x = merge_sort(points, key='x')

    # Divide the points into two halves
    mid = n // 2
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]

    # find the closest pair in each half
    min_left_dist, closest_left = closest_pair_naive(left_half)
    min_right_dist, closest_right = closest_pair_naive(right_half)

    # Determine the minimum distance and closest pair between the two halves
    if min_left_dist < min_right_dist:
        min_dist = min_left_dist
        closest_pair = closest_left
    else:
        min_dist = min_right_dist
        closest_pair = closest_right

    # The points within the strip that are closer than the minimum distance
    strip_points = [point for point in points_sorted_by_x if abs(point[0] - points[mid][0]) < min_dist]
    strip_points_sorted_by_y = merge_sort(strip_points, key='y')

    # Check for closer pairs within the strip
    min_dist, closest_pair = strip_closest(strip_points_sorted_by_y, min_dist, closest_pair)

    # Return the closest pair and its distance
    return min_dist, closest_pair

def strip_closest(strip_points, min_distance, closest_pair):
    """
    Helper function to find the closest pair of points within the strip.
    """
    n = len(strip_points)
    for a in range(n):
        b = a + 1
        while b < n and strip_points[b][1] - strip_points[a][1] < min_distance:
            dist = distance(strip_points[a], strip_points[b])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (strip_points[a], strip_points[b])
            b += 1

    return min_distance, closest_pair

def main():
    # The algorithm with different inputs

    # Sample 1 points
    points1 = [(4, 70), (2, 8), (3, 34), (5, 98), (3, 7)]
    min_distance1, closest_points1 = closest_pair(points1)

    # Confirming the result using the naive algorithm
    min_distance_naive1, closest_points_naive1 = closest_pair_naive(points1)
# Print the result
    print("Closest pair of points (Divide & Conquer): ", closest_points1)
    print("Distance (Divide & Conquer): ", min_distance1)
    print("Closest pair of points (Naive): ", closest_points_naive1)
    print("Distance (Naive): ", min_distance_naive1)
    print()

    # Sample 2 points
    points2 = [(13, 6), (3, 2), (6, 9), (1, 6), (3, 8), (14, 19)]
    min_distance2, closest_points2 = closest_pair(points2)

    # Confirming the result using the naive algorithm
    min_distance_naive2, closest_points_naive2 = closest_pair_naive(points2)

    print("Closest pair of points (Divide & Conquer): ", closest_points2)
    print("Distance (Divide & Conquer): ", min_distance2)
    print("Closest pair of points (Naive): ", closest_points_naive2)
    print("Distance (Naive): ", min_distance_naive2)
    print()

if __name__ == "__main__":
    main()
