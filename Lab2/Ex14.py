#tuples
a = ("dog", "sheep", "bird")
print(a)
#tuples are unchangeable and ordered (==> allow duplicates); can contain different data types
#there is a workaround: change tuple into a list -> change list -> change list into a tuple
#alternate way, through tuple constructor: a = tuple(("dog", "sheep", "bird"))
#a = ("dog") - not a tuple; a = ("dog",) - tuple

a *= 2
print("a * 2 =", a)

print(a.count("dog"))