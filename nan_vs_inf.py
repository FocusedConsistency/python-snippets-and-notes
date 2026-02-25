x = float('nan')
print(x == x)  # False

y = float('inf')
print(y == y)  # True

# float('nan') == float('nan') → False
# NaN represents an undefined or unrepresentable value (e.g., 0.0 / 0.0). 
# By IEEE 754 standard, NaN is not equal to anything, including itself. 
# This behavior signals that a computation went invalid — you can't reliably compare unknown values.
# To check for NaN, use: math.isnan(x) or pandas.isna(x).

# float('inf') == float('inf') → True
# Infinity (inf) represents a well-defined, unbounded value (e.g., 1.0 / 0.0). 
# Positive infinity is considered equal to itself because it's a consistent, predictable limit. 
# This makes practical sense: if two operations overflow, they both reach the same representational ceiling.
