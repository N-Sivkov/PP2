import time


#1
a = []
b = input()
while b != "Done": #cycle only used for arbitrary filling of the list
    a.append(str(b))
    b = input()
a = " * ".join(a)
product = eval(a)
print(product)
print()

#2
a = input()
a1 = list(a)
upper, lower = list(filter(lambda x: x.isupper(), a1)), list(filter(lambda x: x.islower(), a1))
print(f"There are {len(upper)} uppercase and {len(lower)} lowercase letters.")
print()

#3
x1, x2 = slice(len(a) // 2), slice(len(a), len(a) // 2, -1)
aF, aS = a[x1], a[x2]
if aF == aS:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
print()

#4
a = float(input())
delay = int(input())
time.sleep(delay / 1000)
print(f"Square root of {a} after {delay} milliseconds is {pow(a, 1/2)}")
print()

#5
a, b = (84, "Z"), (True, 0)
print(all(a), all(b))