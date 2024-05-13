import sys

a = sys.stdin.readline()
data=list(map(int,a.split()))

n=data[0]
m=data[1]
graph = [[] for _ in range(n+1)]
for i in range(m):
    a = sys.stdin.readline()
    data=list(map(int,a.split()))
    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])

for k in graph:
    k.sort()

for i in range(1,n+1):
    if not graph[i]:
        print("no")
    else :
        str_n=''
        for j in range(len(graph[i])):
            str_n+=str(graph[i][j])
            str_n+=' '
        print(str_n)

