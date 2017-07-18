
import sys
fileName="A-large"
sys.stdin= open(fileName + ".in", "r")
sys.stdout= open(fileName + ".out", 'w')

for t in range(int(input())):

        N= int(input())
        out= "INSOMNIA"
        if N:
            out= N
            digits= set(str(out))
            while len(digits) != 10:
                out+= N
                digits.update(str(out))

        #print(digits)
        print("Case #{}: {}".format(t+1, out))
