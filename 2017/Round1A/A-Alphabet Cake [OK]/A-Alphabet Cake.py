import sys

fileName= "A-large"
sys.stdin= open(fileName + ".in", 'r')
sys.stdout= open(fileName + ".out", 'w')

for t in range(int(input())):
    print("Case #{}:".format(t+1))

    cake= list()
    R, C= map(int, input().split())
    for r in range(R):
        cake.append(str(input()))

    #print(cake, R, C)

    x= 0
    while cake[x] == '?'*C:
        x+= 1
    lastR= str(cake[x])

    for r in range(R):

        if cake[r] == '?'*C:
            cake[r]= str(lastR)
        else:
            lastR= str(cake[r])

        y= 0
        while cake[r][y] == '?':
            y+= 1
        lastC= cake[r][y]

        for c in range(C):
            if cake[r][c] == '?':
                print(lastC, end='')
            else:
                lastC= cake[r][c]
                print(cake[r][c], end='')

        print()
