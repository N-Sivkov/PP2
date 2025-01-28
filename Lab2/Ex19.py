a = [1, 4, 8, 11, "cat", True, 12]
for i in a:
    print(i, end=" ")

for i in range(len(a)):
    print(a[i])
else:
    print("Launch")

for i in range(10, 0, -1):
    if i > 10: continue
    print(i)