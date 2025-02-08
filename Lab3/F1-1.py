from Functions1 import s_v, prime_check


while True:
    a = int(input())
    if not prime_check(a): continue
    print(s_v(a))
    break