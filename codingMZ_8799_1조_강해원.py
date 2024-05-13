#On^2  
import sys

s = int(sys.stdin.readline().strip())
max_c=0
max_s=0
for i in range(1,s+1):
    cnt=0
    for a in range(1,i//3+1):
        flag=False
        for b in range(a,(i-a)//2+1):
            c= i-a-b
            if a**2 +b**2 == c**2:
                cnt+=1
                flag=True
            if flag:
                flag=False
                break
    if cnt>max_c:
        max_c=cnt
        max_s=i
print(str(max_s)+' '+str(max_c))
    