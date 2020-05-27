n = int(input())
k = int(input())
i = k
f = []
for m in range(k):
    f.append(int(input()))

while (i > 0 and (f[i - 1]) == (n - k + i)):
    i = i - 1
if(i>= 1):
    f[i - 1]=(f[i - 1])+1

    j = i-1 + 1
    while j<k:
        f[j]=(f[i - 1])+j-i+1
        j = j + 1
else:
    for i in range(k):
        f[i]=i+1;
print(f)