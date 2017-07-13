import sys
sys.stdin= open("D-sample.in", "r")
#sys.stdout= open("D-.out", 'w')


for t in range(int(input())):

    N, M= map(int, input().split())

    grid= {}
    row, col, sub, add= set(range(N)), set(range(N)), set(range(-N + 1, N)), set(range(2*N - 1))
    changes= {}

    for m in range(M):
        value, i, j= input().split()
        i, j= int(i)-1, int(j)-1

        grid[i,j]= value
        if value in ('x', 'o'):
            row.remove(i)
            col.remove(j)
        if value in ('+', 'o'):
            sub.remove(j-i)
            add.remove(i+j)

    print(sub)

    for i in [0, N-1]:
        for j in range(N):

            if j-i in sub and i+j in add:

                c= ''
                if (i, j) not in grid:
                    c= '+'
                elif grid[i, j] == 'x':
                    c= 'o'
                else:
                    assert False, str(grid[i, j])

                grid[i, j]= c
                changes[i, j]= c
                sub.add(j-i)
                add.add(i+j)


    for i in row:
        for j in col:

            c= ''
            if (i, j) not in grid:
                c= 'x'
            elif grid[i, j] == '+':
                c= 'o'
            else:
                assert False, str(grid[i, j])

            grid[i, j]= c
            changes[i, j]= c
            row.add(i)
            col.add(j)


    points= 0
    for (i, j) in grid:
        if grid[i, j] == 'o':
            points+= 2
        else:
            points+= 1

    #print(grid)
    print("Case #{}: {} {}".format(t+1, points, len(changes)))
    #for (i, j) in changes:
    #    print("{} {} {}".format(changes[i, j], i, j))
