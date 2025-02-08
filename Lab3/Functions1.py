import math
import random


def g_2_o(n):
    return n * 28.3495231


def F_2_C(n):
    return (5 / 9) * (n - 32)


def solve(numheads, numlegs):
    #since a rabbit's legs are 2 times the quantity of a chicken's, the average ratio will be 1:2
    return numheads / 3, numheads / 3 * 2


def prime_check(n):
    prime = True
    for i in range (2, n):
        if n % i == 0:
            prime = False
            break
    return prime


def filter_prime(n):
    return list(filter(lambda x: prime_check(x), n))


def permuts(n, a=0):
    if a == len(n):
        print("".join(n), end=" ")
    for i in range(a, len(n)):
        N = list(n)
        N[a], N[i] = N[i], N[a]
        permuts(N, a + 1)


def reverse_sentence(n):
    N = n.split()
    m = ""
    for i in range(len(N) - 1, -1, -1):
        m += N[i]
        if i != 0: m += " "
    return m


def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i] == 3: return True
    return False


def spy_game(nums):
    for i in range(2, len(nums)):
        if nums[i - 2] == nums[i - 1] == 0 and nums[i] == 7: return True
    return False


def s_v(n):
    return 4 / 3 * math.pi * n ** 3


def unique_list(n):
    N = []
    for i in n:
        if i not in N: N.append(i)
    return N


def palindrome(n):
    a = True
    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            a = False
            break
    return a


def histogram(n):
    for i in n:
        print("*" * i)


def GtN():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    guess = 99
    attempts = 1
    while guess != num:
        guess = int(input("Take a guess.\n"))
        if guess < num:
            print("Your guess is too low.")
            attempts += 1
        elif guess > num:
            print("Your guess is too high.")
            attempts += 1
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")