import re


with open("row.txt", "r", encoding="utf-8") as file:
    txt = file.read()

#1
a = re.search("ab*", txt)
print(a)
print()

#2
a = re.search("ab{2,3}", txt)
print(a)
print()

#3
a = re.findall("._.", txt)
print(a)
print()

#4
a = re.findall("[A-ZА-Я][a-zа-я]+", txt)
print(a)
print()

#5
a = re.findall("a.+b$", txt)
print(a)
print()

#6
a = re.sub("\s|,|.", ":", txt)
print(a)
print()

#7
a = re.sub("_([a-zа-я])", lambda x: x.group(1).upper(), txt)
print(a)
print()

#8
a = re.split("[A-ZА-Я]", txt)
print(a)
print()

#9
a = re.sub(r"(?<!^)([A-ZА-Я])", r" \1", txt)
print(a)
print()

#10
a = re.sub("([a-zа-я])([A-ZА-Я])([a-zа-я])", lambda x: x[0] + "_" + x[1].lower(), txt)
print(a)
print()