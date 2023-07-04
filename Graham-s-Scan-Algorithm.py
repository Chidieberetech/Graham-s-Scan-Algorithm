import matplotlib.pyplot as plt
import math

# Graham's Scan Algorithm   for   Convex Hull Assignment.

def merge_sort(points, key='p0'):
    """
    Sorts a list of points based on their polar angle with respect to p0.
    Args:points (list): List of points to be sorted.
    p0 (tuple): Origin point with respect to which the polar angles are calculated.
    Returns:list: Sorted list of points.
    """

    # Base case: If the list contains only one point, return the list   (it is already sorted)
    if len(points) <= 1:
        return points

    # Finding the middle point in the list  (the pivot) and dividing the list into two halves
    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]

    # Sorting the left and right portions recursively
    left_sorted = merge_sort(left_half, key)
    right_sorted = merge_sort(right_half, key)

    #
    return merge(left_sorted, right_sorted, key)


def merge(left, right, key):
    """
    Merges two sorted lists of points based on their polar angles with respect to p0.
    Args:
    left (list): Sorted list of points.
    right (list): Sorted list of points.
    p0 (tuple): Origin point with respect to which the polar angles are calculated.
    Returns:
    list: Merged and sorted list of points.
    """

    merged = []  # Listing to store the merged points
    left_index = right_index = 0

    # Comparing the polar angles of the points in the left and right lists
    while left_index < len(left) and right_index < len(right):

        # Compute the polar angles of the points
        left_angle = polar_angle(left[left_index], key)
        right_angle = polar_angle(right[right_index], key)

        # Comparing the angles and append the point with the smaller angle to the merged list
        if left_angle <= right_angle:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Appending the remaining points from the left and right lists (if any)
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

#   Computing the polar angle of a point with respect to p0.
def polar_angle(point, key):
    """
    Computing the polar angle of a point with respect to p0.
    """
    dx = point[0] - key[0]
    dy = point[1] - key[1]
    return math.atan2(dy, dx)


def graham_scan_algorithm(points):
    """
    Computing the convex hull of a set of points using Graham's Scan algorithm.
    Args:
    points (list): List of points.
    Returns:
    list: Convex hull points in counterclockwise order.
    """

    # Finding the lowest point in the list (lowest y-coordinate)    (p0)    (lowest_point)
    lowest_point = min(points, key=lambda point: (point[1], point[0]))

    # Sorting the points based on their polar angles with respect to p0   (lowest_point)
    sorted_points = sorted(points, key=lambda point: polar_angle(point, lowest_point))

    # Creating a stack and pushing the first two points onto the stack  (lowest_point, sorted_points[1])
    stack = [lowest_point, sorted_points[1]]

    # Iterating over the remaining points in the list and pushing them onto the stack   (sorted_points[2:])
    for point in sorted_points[2:]:
        while len(stack) > 1 and is_clockwise(stack[-2], stack[-1], point):
            stack.pop()

        stack.append(point)
    # Returning the stack
    return stack

#       Checking if the points p1, p2, and p3 form a clockwise turn.
def is_clockwise(p1, p2, p3):
    """
    Checks if the points p1, p2, and p3 form a clockwise turn.

    Args:
        p1 (tuple): First point.
        p2 (tuple): Second point.
        p3 (tuple): Third point.

    Returns:
        bool: True if the points form a clockwise turn, False otherwise.
    """

    return (p2[1] - p1[1]) * (p3[0] - p2[0]) > (p2[0] - p1[0]) * (p3[1] - p2[1])


# List of points    (points)    and origin point    (p0)    (0, 0)
points = [(1, 2), (-3, 4), (5, 6), (7, 8), (9, 10)]
p0 = (0, 0)

# Sorting the points based on their polar angles with respect to p0   (lowest_point)
sorted_points = merge_sort(points, p0)

# Computing the convex hull using Graham's Scan algorithm
convex_hull = graham_scan_algorithm(sorted_points)

#   Printing the convex hull    (convex_hull)       (x_hull, y_hull)    (x_sorted, y_sorted)    (sorted_points)
x_sorted = [point[0] for point in sorted_points]
y_sorted = [point[1] for point in sorted_points]
x_hull = [point[0] for point in convex_hull]
y_hull = [point[1] for point in convex_hull]

# Plotting the points and the convex hull   (x_sorted, y_sorted)    using matplotlib    (plt)   (pyplot)
plt.scatter(x_sorted, y_sorted, c='blue', label='Sorted Points')
plt.scatter(x_hull, y_hull, c='red', label='Convex Hull')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Convex Hull')
plt.legend()
plt.grid(True)
plt.show()


# Thank you for teaching us Algorithm and Data Structure, Professor!