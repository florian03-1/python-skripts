n = int(input())

l = []

for i in range(1, n):
    if (i < 3):
        l.append(1)
    else:
        l.append(l[len(l) - 1] + l[len(l) -2])

    print(i, ": ", l[i-1])
