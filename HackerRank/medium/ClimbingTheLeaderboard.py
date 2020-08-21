from bisect import bisect_right

def climbingLeaderboard(scores, alice):
    scores= sorted(list(set(scores)))
    alicerank=[]
    for i in alice:
        alicerank.append(len(scores) - bisect_right(scores, i) + 1)


    print(alicerank)

if __name__ == '__main__':

    result = climbingLeaderboard([100,100,50,40,40,20,10], [2,3,3,4,5,25,50,100,120,150,180,190])

    """
     i=0
    j=(len(scores)-1)
    while j>-1:

        if j == 0 and i < len(alice):
            alicerank.append(1)
            i += 1

        if i >= (len(alice)):
            break

        if scores[j] > alice[i]:
            alicerank.append(rank[j] + 1)
            i += 1
        elif scores[j] == alice[i]:
            alicerank.append(rank[j])
            i += 1
        else:
            if j > 0:
                j -= 1

    """
    """
    for i in range(len(alice)):
        if alice[i]<scores[len(scores)-1]:
            alicerank.append(rank[len(rank)-1]+1)
        else:
            pos=scores.index(min(scores, key=lambda x: abs(x - alice[i])))
            alicerank.append(rank[pos])
    #search bisect
    
    """


    """ 
    for i in range(len(alice)):
        for j in range(len(scores)):
            if alice[i]>=scores[j]:
                alicerank.append(rank[j])
                break
            elif j==(len(scores)-1):
                alicerank.append(rank[j]+1)

    print(alicerank)
    """
