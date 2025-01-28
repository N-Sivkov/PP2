#lists
a = [1, 13, "apple", True, 22]
print(a)
print(a[3])
print(*a)
print(*a[-1:-(len(a) + 1):-1])
print()

b = input()
print("Search result for '" + str(b) + "':", b in a)
print()

index, value = int(input()), input()
a[index] = value
print("Element", index + 1, "changed to", "'" + value + "':", a)
print()

index1, index2, value = int(input()), int(input()), input()
a[index1:index2] = [value]
print("Elements from", index1 + 1, "to", index2 + 1, "replaced with '" + value + "':", a)
print()

index, value = int(input()), input()
a.insert(index, value)
print(f"'{value}' inserted to position {index}:", a)
print()

value = input()
a.append(value)
print(f"{value} added to the end of the list:", a)
print()

a1, a2, a3 = [1, 2, 3], [13, 8, 24], (4, 11, 9)
print(f"{a1} + {a2} =", a1.extend(a2))
print(f"{a1} + {a3} =", a1.extend(a3))
print()

value = input()
a.remove(value)
print(a)

a.pop(1)
#del a[1] - the same; if left without brackets - the whole list will be deleted; a.clear() will leave the list, but will clear it
print("the second (1) element removed:", a)
#if left without arg-s, the last elem will be removed

[print(i, end=" ") for i in a if len(i) > 2]

a.sort(reverse=True)
#a.sort(key=some_function)
#Example: a.sort(key=str.lower) --> case-sensitive sort

b = a.copy() #== b = a[:]