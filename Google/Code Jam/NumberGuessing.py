import sys


def guess(a, b):
    guessed = (a + b) // 2
    print(guessed)
    sys.stdout.flush()
    res = input()
    if res == "CORRECT":
        return
    elif res == "TOO_SMALL":
        a = guessed + 1
    else:
        b = guessed - 1
    guess(a, b)


cases = int(input())
for i in range(cases):
    a, b = map(int, input().split())
    n = int(input())
    guess(a + 1, b)
