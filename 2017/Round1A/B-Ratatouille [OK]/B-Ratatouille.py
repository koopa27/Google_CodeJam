import sys
import math

fileName= "small"
sys.stdin= open(fileName + ".in", 'r')
sys.stdout= open(fileName + ".out", 'w')

for t in range(int(input())):
    nbIngredients, nbPackages= map(int, input().split())
    kits= list()

    for s in [float(_) for _ in input().split()]:
        kits.append(sorted([float(p)/s for p in input().split()]))

    out= 0
    while all(kits):

        k= 0
        for i in range(nbIngredients):
            if kits[i][0] < kits[k][0]:
                k= i

        left, right= math.ceil(kits[k][0]/1.1), math.floor(kits[k][0]/0.9)
        if left > right:
            kits[k].pop(0)

        else:
            KO= False
            for kit in kits:
                if math.ceil(kit[0]/1.1) > right:
                    KO= True
                    break

            if KO:
                kits[k].pop(0)
            else:
                out+= 1
                for kit in kits:
                    kit.pop(0)

    print("Case #{}: {}".format(t+1, out))
