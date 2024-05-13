import sys

li=[[] for _ in range(4)]
for i in range(4):
    a = sys.stdin.readline()
    for j in a:
        li[i].append(j)
cnt=0
flag=False
for i in range(3):
    for j in range(3):
        for k in range(2):
            for t in range(2):
                if li[i+k][j+t]=='X':
                    cnt+=1
        if cnt>=3:
            flag=True
        cnt=0

if flag:
    print("yes")
else : 
    print("no")