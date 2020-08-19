def pickingNumbers(a):
    numbers=sorted(a)
    maxvalue=0
    cont=1
    for i in range(1,len(numbers)):

        if (numbers[i]-numbers[i-1])<2:
            cont+=1
        else:

            if maxvalue<cont:
                maxvalue=cont
            cont=1
    print(maxvalue)
if __name__ == '__main__':


    result = pickingNumbers([4,5,6,3,3,1])

