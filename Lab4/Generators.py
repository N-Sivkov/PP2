#1
def sq(n):
    for i in range(1, n + 1):
        yield i ** 2


#2
def evs(n):
    for i in range(1, n):
        if i % 2 == 0: yield i


#3
def tfs(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 4 == 0: yield i


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


#5
def tozero(n):
    for i in range(n, -1, -1):
        yield i


#2
n = int(input())
print(*[i for i in evs(n)], sep=", ")
print()

#4
for i in squares(3, 11):
    print(i, end=" ")
print()