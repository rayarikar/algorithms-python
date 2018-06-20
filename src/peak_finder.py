# Find a peak element in 1D array
# Assumptions:  - The elements will always be in increasing - decreasing - increasing order or vice versa
#               - You will not be given all elements which are same in value (a peak will always exist)
# Sample Input: [1,4,5,6,4,2,1] ==> 6
#               [1,4,5,6,4,2,1,8,2,1] ==> 6 or 8
# Time complexity: O(log(n))


def one_dimensional_peak(input):
    print input[:]
    start, end = 0, len(input)
    if len(input) <= 1:
        print "No peak can be computed for this input"
    while start < end:
        mid = (start + end) / 2
        if input[mid] > input[mid - 1] and input[mid] > input[mid + 1]:
            print "Peak for the given input: " + str(input[mid])
            break
        if input[mid - 1] > input[mid]:
            end = mid
        elif input[mid + 1] >= input[mid]:
            start = mid
        else:
            print "Ideally we should never come here"


def test_one_dimensional_peak():
    input1 = [1, 3, 4, 6, 8, 2, 1]
    input2 = [1, 4, 5, 6, 4, 2, 1, 8, 2, 1]
    one_dimensional_peak(input1)
    one_dimensional_peak(input2)


# Given a 2D array where each column has a peak, find a global maximum in the 2D array
# Assumptions:    - Each column will always have a peak
#                 - The elements in each column will always be in increasing - decreasing - increasing order or vice
#                   versa
#                 - The elements in each column will never be all equal in value (i.e. a peak per column
#                   will always exist)
#                 - A global maximum is defined as an element which is greater than its
#                   immediate top, bottom, left and right element
#                 - If there are more than 1 global maximums, return any 1

def two_dimensional_peak_finder(input):
    print "Solution goes here"


test_one_dimensional_peak()
