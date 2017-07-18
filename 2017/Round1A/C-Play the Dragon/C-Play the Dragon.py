import sys
import math

fileName= "small"
sys.stdin= open(fileName + ".in", 'r')
sys.stdout= open(fileName + ".out", 'w')

for t in range(int(input())):
    out= "IMPOSSIBLE"
    Hd0, Ad0, Hk0, Ak0, B0, D0= map(float, input().split())

    nAd= math.ceil(Hk0/Ad0)
    nAk= math.ceil(Hd0/Ak0)

    if B0:
        nB= (math.sqrt(B0*Hk0)-Ad0)/B0
        nBA= math.ceil(Hk0/(Ad0 + nB*B0)+nB)
        nAd= min(nBA, nAd)

    if nAd <= nAk:
        out= nAd

    elif nAk == 1 or (nAk == 2 and not D0):
        pass

    elif not D0:
        nC= math.ceil(nAd/nAk) -1
        out= nAd + nC

    else:
        nC, nD= 0, 0
        Hd, Ak= Hd0, Ak0
        while nAk < nAd and Ak > 0:
            nD+= 1
            if (Hd - Ak + nD*D0) > 0 :
                Ak-= nD*D0
                if not Ak:
                    break
                #print(Hd, Ak)
                nAk= math.ceil(Hd/Ak)
                Hd-= Ak
            else:
                nC+= 1
                Hd= Hd0



        out= nAd + nD + nC

    print("Case #{}: {}".format(t+1, out))
