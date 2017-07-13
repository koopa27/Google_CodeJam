
import sys
sys.stdin= open("A_large.in", "r")
sys.stdout= open("A_large.out", 'w')

for l in range(int(input())):

        nbFlips= 0
        line= input()
        pancakes= [p=='+' for p in line.split()[0]]
        flip= int(line.split()[1])

        print(pancakes, file= sys.stderr)

        for i in  range(len(pancakes) - flip + 1):
            if not pancakes[i]:
                nbFlips+= 1
                pancakes[i:i+flip]= [not p for p in pancakes[i:i+flip]]

        if not all(pancakes):
            nbFlips= 'IMPOSSIBLE'
        print("Case #" + str(l+1) + ": " + str(nbFlips))
