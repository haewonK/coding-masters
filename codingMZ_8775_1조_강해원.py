import sys

def dfs(v):
    if visited[v]:
        return
    else :
        visited[v]=True
        


n= int(sys.stdin.readline())
m= int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a = sys.stdin.readline()
    data=list(map(int,a.split()))
    graph[data[0]].append(data[1], data[2]) # 노드, 가중치 저장  

a = sys.stdin.readline()
data=list(map(int,a.split()))

start=data[0]
end=data[1]
visited=[False for _ in range(n+1)]


