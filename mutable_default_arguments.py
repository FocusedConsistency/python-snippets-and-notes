def append_to_list(item, lst=[]):
    lst.append(item)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2] — not [2]!

# Using None instead
def append_to_list(item, lst=None):
    if lst is None:
        lst = []  # Always creates a fresh list
    lst.append(item)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [2] — expected behavior
