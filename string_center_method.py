# Using a string building example using a list, which centers a string between asterisks with a line length limit of 30.
class Category:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        strings = []
        line_len = 30
        index_of_name = (line_len - len(self.name)) // 2
        strings.extend(["*"] * (index_of_name))
        strings.append(self.name)
        strings.extend(["*"] * (line_len - len(strings)))
        title = ''.join(strings)
        return title
# returns *************Food*************
food = Category('Food')
print(food)

# Can simply be done using a center method instead
def __str__(self):
    return self.name.center(30, '*')
# returns *************Food*************

# For more flexibility f-strings can be utilized
def __str__(self):
    return f"{self.name:*^30}"
# returns *************Food*************

# String methods
text = "Hello"
text.ljust(10)   # 'Hello     ' (left-aligned)
text.rjust(10)   # '     Hello' (right-aligned)
text.center(10)  # '  Hello   ' (centered)

# Python 3.6+
f"{text:<10}"    # 'Hello     ' (left-aligned)
f"{text:>10}"    # '     Hello' (right-aligned)
f"{text:^10}"    # '  Hello   ' (centered)
