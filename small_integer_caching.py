a = 256; b = 256
print(a is b)  # True
a = 257; b = 257
print(a is b)  # False

# The behavior occurs due to integer caching in CPython
# Python caches integers in the range -5 to 256 for performance.  These integers are reused as singleton objects.
# When you write a = 256; b = 256, both variables refer to the same cached object, so a is b returns True. 
# For integers outside this range (like 257), Python creates separate objects each time, so a is b returns False even if their values are equal. 
