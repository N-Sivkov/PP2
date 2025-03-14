import os


#1
path = "C:\\Users\\user\\le code\\Lab6"
dl = os.listdir(path)
print(f"Files and directories in '{path}': \n{dl}\n")

#2
print(path)
print(f"Exists: {os.path.exists(path)} \nReadable: {os.access(path, os.R_OK)} \nWritable: {os.access(path, os.W_OK)} \nExecutable: {os.access(path, os.X_OK)} \n")

#3
path += "\\builtin-functions.py"
if os.path.exists(path):
    dp = os.path.dirname(path)
    filename = ""
    for i in range (len(dp) + 1, len(path)):
        filename += path[i]
    print("Filename:", filename)
    print("Directory portion:", dp, "\n")

#4
f = open("sample.txt", "r")
count = 0
for i in f:
    count += 1
print(count)
f.close()

#5
a = "Sample text to be converted into a list".split()
f = open("L2F.txt", "x")
f.write(" ".join(a))
f.close()

#6
names="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in names:
    f = open(f"{i}.txt", "x")
    f.close()

#7
f = open("sample.txt", "r")
text = f.read()
f.close()
f = open("Copy.txt", "x")
f.write(text)
f.close()

#8
path = "C:\\Users\\user\\le code\\Lab6\\Copy.txt"
z = input("Input anything to start the deletion procedure: ")
print(f"Exists: {os.path.exists(path)} \nReadable: {os.access(path, os.R_OK)} \nWritable: {os.access(path, os.W_OK)} \nExecutable: {os.access(path, os.X_OK)}")
print("Deleting the file...")
os.remove(path)
path = "C:\\Users\\user\\le code\\Lab6\\"
for i in names:
    path1 = path + i + ".txt"
    os.remove(path1)
path1 = path + "L2F.txt"
os.remove(path1)