tc = int(input())
x = 1
while(tc>0):
    y = 0
    green = 0
    yellow = 0
    N,K = [int(x) for x in input().split(" ")]
    l1 = [int(x) for x in input().split(" ")]
    for i in range(0,N-1):
        if(l1[i]-1 == l1[i+1]):
            yellow = i
            green = yellow + 1
            temp = green
            for j in range(temp , N-1):
                if(l1[j]-1 == l1[j+1]):
                    green = green+1
                    if(green-yellow == K-1):
                        y = y+1
                        break
                else:
                    break
            #print(green,yellow)
    print("Case #{}: {}".format(x,y))
    x = x+1
    tc = tc-1
