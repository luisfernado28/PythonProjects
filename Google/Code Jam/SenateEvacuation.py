import operator


def solve(senators):
    eliminated = max(senators.items(), key=operator.itemgetter(1))[0]

    print(eliminated,end=' ')
    senators[eliminated] -= 1
    if senators[eliminated] <= 0:
        del senators[eliminated]
    if len(senators) == 2:
        a, b = senators.keys()
        c = a + b
        print(c)
        return
    solve(senators)


t = int(input())
for i in range(t):
    parties = int(input())

    senli = list(map(int, input().split()))
    senate = {}
    for j in range(parties):
        letter = chr(j + 65)
        senate[letter] = senli[j]
    print("Case #{}: ".format(i+1), end='')

    solve(senate)
