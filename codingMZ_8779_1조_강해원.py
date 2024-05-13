import sys

a = sys.stdin.readline()
data=list(map(int,a.split()))
answer=''
n=data[0]
k=data[1]

a = sys.stdin.readline()
for i in range(n):
    for j in range(k):
        answer+=a[i]
print(answer)