# Instead of this
def count_change(change):
    total = sum(change)
    dollars = total // 100
    cents = total % 100
    return f"${dollars}.{cents:02d}"
  
count_change([25, 10, 5, 1]) # returns "$0.41"

# We can use divmod
def count_change(change):
    total = sum(change)
    dollars, cents = divmod(total, 100)
    return f"${dollars}.{cents:02d}"
