import sys
sys.stdin= open("B_large.in", "r")
sys.stdout= open("B_large.out", 'w')


for l in range(int(input())):

    number= str(input())

    while list(number) != sorted(list(number)):

        previous= '0'
        for i in range(len(number)):

            if number[i] < previous:
                left= str(int(number[:i])-1)
                right= '9'*(len(number[i:]))
                number= left + right

            previous= number[i]

    print("Case #" + str(l+1) + ": " + str(int(number)))
