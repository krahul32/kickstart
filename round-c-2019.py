# Google Kick Start 2019 Round C Problem

import numpy as np
tc = int(input())
c = 1
while(tc):
    L = [int(x) for x in input().split()]
    (N,R,C,SR,SC) = (L[0],L[1],L[2],L[3]-1,L[4]-1)

    #setting current row and current column to start, initially
    (CR,CC) = (SR,SC)

    #initializing grid with the given size
    arr = np.arange(R*C).reshape(R,C)
    arr = np.zeros((R,C))

    #setting start point (1 represent visited location)
    arr[SR][SC] = 1

    #taking N input directions to move robot and storing it in the list
    dir_list = [str(x) for x in input()]

    for i in dir_list:
        if i == 'N':
            while (arr[CR][CC]!=0):              
                (CR,CC) = (CR-1,CC)              #to move NORTH, we decrease row by 1. Column would be same.
            arr[CR][CC] = 1
        elif i == 'S':
            while (arr[CR][CC]!=0):              #moving towards SOUTH untill we get a non visited place.
                (CR,CC) = (CR+1,CC)              #to move NORTH, we increase row by 1. Column would be same.
            arr[CR][CC] = 1
        elif i == 'E':
            while (arr[CR][CC]!=0):              #moving towards EAST untill we get a non visited place.
                (CR,CC) = (CR,CC+1)              #to move NORTH, we increase column by 1. Row would be same.
            arr[CR][CC] = 1
        elif i == 'W':
            while (arr[CR][CC]!=0):              #moving towards WEST untill we get a non visited place.
                (CR,CC) = (CR,CC-1)              #to move NORTH, we decrease column by 1. Row would be same.
            arr[CR][CC] = 1
    print("Case #{0}: {1} {2}".format(c,CR+1,CC+1))
    c+=1
    tc-=1
