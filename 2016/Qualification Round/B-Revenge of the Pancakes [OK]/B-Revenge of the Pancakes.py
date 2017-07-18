
import sys
fileName="large"
sys.stdin= open(fileName + ".in", "r")
sys.stdout= open(fileName + ".out", 'w')

for t in range(int(input())):

    pancakes= [ p == '+' for p in input()]
    pancakes.reverse()

    out= 0
    i= 0
    while not all(pancakes):

        if not pancakes[i]:

            j= i
            if pancakes[-1]:
                while not pancakes[i]:
                    i+= 1

            save= pancakes[i:]
            save= [not p for p in save]
            save.reverse()
            pancakes[i:]= save

            out+= 1
            i= j

        else:
            i+= 1


    print("Case #{}: {}".format(t+1, out))
