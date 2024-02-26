# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


# all elements in the array will be integer
# if the array is empty, return an empty list

# [3, 5, 7, -2, -3, 5, 7, -9]
# if the array is empty, return an empty list
# look at every element in the list
# if the element is positive, add 1 to the positive count
# if the element is negative, add the negative value to the gative_sum 
# once we've looked at every element, return a list with positive count as first value, negative sum as second
# [5, -14]


def solution(arr_of_nums):
    if not arr_of_nums:
        return []
    positive_count = 0
    negative_sum = 0
    for element in arr_of_nums:
        if element > 0: 
            positive_count += 1
        elif element < 0:
            negative_sum += element
    return [positive_count, negative_sum]

