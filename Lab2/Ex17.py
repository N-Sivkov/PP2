a, b = 14, 28
if a > b:
    print("Impossible")
elif (a == b and b == a) or (b == a and a == b):
    print("Equal")
else:
    print()

if a < b: pass

print("Impossible") if a > b else print("Equal") if a == b else print()