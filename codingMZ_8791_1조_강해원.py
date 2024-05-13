import sys

a = sys.stdin.readline()
data=list(map(int,a.split()))
n=data[0]
k=data[1]

cup=[]
for i in range(n):
    cup.append(i+1)

for i in range(k):
    a = sys.stdin.readline()
    data=list(map(int,a.split()))
    s=data[0]
    e=data[1]
    temp=cup[s-1]
    cup[s-1]=cup[e-1]
    cup[e-1]=temp

ans=input()
a=0
for i in cup:
    a+=1
    if i==int(ans):
        print(a)

