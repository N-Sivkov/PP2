#variable types cannot be combined like this:
"""
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

# - - -

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# - - -

price = 59
txt = f"The price is {price} dollars"
print(txt)

# - - -

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# - - -

txt = f"The price is {20 * 59} dollars"
print(txt)