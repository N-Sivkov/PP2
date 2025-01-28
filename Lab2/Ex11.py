a = 8 > 11
print("8 > 11:", a)
print("11 = 13:", 11 == 13)
print("228 < 1221:", True)
print()

print(bool("Abyrvalg"))
print(bool(0))
print()

a, b = int(input()), int(input())
if (a > b):
    print(a, ">", b)
else:
    print(a, "<=", b)