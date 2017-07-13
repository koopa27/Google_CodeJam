import sys
import heapq
sys.stdin= open("C-small1.in", "r")
sys.stdout= open("C-small2.out", 'w')


for l in range(int(input())):

    N, K= map(int, input().split())

    gaps= [-N]
    gapsCount= {N: 1}
    left, right= 0, 0
    while True:

        gap= -heapq.heappop(gaps)
        count= gapsCount[gap]
        del gapsCount[gap]

        left, right= (gap-1)//2, gap//2
        if K <= count:
            break

        K-= count
        for g in [left, right]:
            if g not in gapsCount:
                heapq.heappush(gaps, -g)
                gapsCount[g]= 0
            gapsCount[g]+= count

    print("Case #" + str(l+1) + ": " + str(right) + " " + str(left))
