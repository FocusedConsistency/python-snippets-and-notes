# Pattern that is commonly used for range-based categorization, such as letter grades or bins. O(log n)

from bisect import bisect

def get_category(n):
    if not 1 <= n <= 50:
        raise ValueError("Number must be between 1 and 50")
    breakpoints = [10, 20, 30, 40]
    categories = "ABCDE"
    return categories[bisect(breakpoints, n)]

# Returns 'A' for n in 1-9, 'B' for n in 10-19, ..., 'E' for n in 40-50   
