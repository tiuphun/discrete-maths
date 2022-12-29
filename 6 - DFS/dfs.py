import sys
def input():
    [n, m] = [int(x) for x in sys.stdin.readline().split()]
    A = [[] for v in range(n+1)] #A[v]: list of adjacent nodes of v
    for i in range(m):
        [u, v] = [int(x) for x in sys.stdin.readline().split()]
        A[u].append(v)
        A[v].append(u)
    return n, m, A
def dfs(u):
    id[u] = cnt 
    for v in A[u]:
        if id[v] == 0:
            dfs(v)
def dfsG():
    global cnt 
    for u in range(1, n+1):
        if id[u] == 0: #node v is not visited
            cnt += 1 #one more connected component is started to be constructed
            dfs(u)
n, m, A = input()
cnt = 0 # number of connected components being constructed
id = [0 for v in range(n+1)]
d = [0 for v in range(n+1)] #d[v]: time-point node v is visited
f = [0 for v in range(n+1)] #f[v]: time-point node v finished exploration (traversal)
t = 0 # global discrete time variable
dfsG()
print('number of connected components is ', cnt)
for c in range(1, cnt+1):
    #collect node in the connected component c
    print('connected component ', c, ': ')
    for v in range(1, n+1):
        if id[v] == c:
            print(v, end = ' ')
    print(' ')
for v in range(1, n+1):
    print('node ', v, ': d = ', d[v], ', f = ', f[v])