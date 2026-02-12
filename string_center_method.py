# Using a string building example using a list, which centers a string between asterisks with a line length limit of 30.
def __str__(self):
    strings = []
    line_len = 30
    index_of_name = (line_len - len(self.name)) // 2
    strings.extend(["*"] * (index_of_name))
    strings.append(self.name)
    strings.extend(["*"] * (line_len - len(strings)))
    title = ''.join(strings)
    return title

# Can simply be done using a center method instead
def __str__(self):
    return self.name.center(30, '*')
