import sys

# Dynamic arrays implemented via underlying static arrays with geometric over-allocation.
# Example how memory capacity grows behind the scenes with incremental steps.
lst = []
for i in range(10):
    print(f"Length: {len(lst):2}, Capacity: {sys.getsizeof(lst):3} bytes")
    lst.append(i)

# Length:  0, Capacity:  56 bytes
# Length:  1, Capacity:  88 bytes
# Length:  2, Capacity:  88 bytes
# Length:  3, Capacity:  88 bytes
# Length:  4, Capacity:  88 bytes
# Length:  5, Capacity: 120 bytes
# Length:  6, Capacity: 120 bytes
# Length:  7, Capacity: 120 bytes
# Length:  8, Capacity: 120 bytes
# Length:  9, Capacity: 184 bytes
