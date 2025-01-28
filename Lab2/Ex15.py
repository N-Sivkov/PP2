#sets
a = {"dog", "sheep", "bird"}
#alternative way: a = set(("dog", "sheep", "bird"))
#unordered, unchangeable, do not allow duplicates; 
#True and 1, False and 0 are considered the same values --> are not allowed together as duplicates

[print(i, end=" ") for i in a] #since elem-s cannot be accessed with indexes, the only way is to loop through the set

b = {"badger", "horse"}
c = ["goat", "fish"]
print("a + b =", a.update(b)) 
print("a + c =", a.update(c))
#update == extend from lists

value = input()
#a.remove(value) --> will raise an error if value not in a
a.discard(value)    #will not raise an error
#pop() also works, but removes a random item

del a # --> deletes the set completely