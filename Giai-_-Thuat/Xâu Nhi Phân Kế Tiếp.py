s = int(input())
n = 0
h = 0
while (n < s):
    g = 0
    a = 0
    e = 0
    n = n + 1
    a = input()
    d = len(a)
    for b in a:
        d = d - 1
        c = int(b) * (2 ** d)
        e = e + c
    g = e + 1
    print(g)
    i = ""
    j = ""
    while (g != 0):
        h = g % 2
        g = g // 2
        i = str(h)
        print(i)
        j = i + j
    print(j)
