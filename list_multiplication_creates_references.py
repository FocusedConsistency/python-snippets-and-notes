grid = [[]] * 3
grid[0].append(1)
print(grid)
# [[1], [1], [1]]
# This is because all 3 cells share the same reference.
# We can confirm this by comparing memory addresses.
print(id(grid[0]) == id(grid[1]) == id(grid[2]))
# True

grid = [[] for _ in range(3)]
grid[0].append(1)  # Only affects the first sublist
print(grid)  # [[1], [], []]
print(id(grid[0]) == id(grid[1]) == id(grid[2]))
# False
