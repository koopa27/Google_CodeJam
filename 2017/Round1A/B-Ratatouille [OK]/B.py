import math

import sys
fileName= "sample"
sys.stdin= open(fileName + ".in", 'r')

T = int(input())
for t in range(T):
    N, P = map(int, input().split())
    R = list(map(float, input().split()))
    V = list()

    for i in range(N):
        Q = list(map(float, input().split()))
        V.append(sorted([q/R[i] for q in Q]))

    print(V)
    out = 0
    while all(V):
        k = 0
        for i in range(1,N):
            if V[i][0] < V[k][0]:
                k = i
        mins = math.ceil(V[k][0] / 1.1)
        maxs = math.floor(V[k][0] / .9)
        if mins > maxs:
            V[k].pop(0)
        else:
            bad = False
            for v in V:
                if v[0] > maxs * 1.1:
                    bad = True
                    break
            if bad:
                V[k].pop(0)
            else:
                for v in V:
                    v.pop(0)
                out += 1
    print("Case #%d: %d" % (t + 1, out))
