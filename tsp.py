import sys

def input():
    [n] = [int(x) for x in sys.stdin.readline().split()]
    c = []
    for i in range(n):
        a = [int(x) for x in sys.stdin.readline().split()]
        c.append(a)
    return n, c

def solution():
    global fmin
    # compare current solution with best solution found so far
    # update if better
    if f + c[x[k]][c[1]] < fmin:
        fmin = f + c[x[k]][c[1]]
        print('new best: ', fmin)
    
    
def trial(k): # partial route x[1] + x[2]
    global f
    for v in range(1, n+1):
        if visited[v] == False:
            x[k] = v
            visited[v] = True
            f = f + c[x[k-1]][c[k]]
            if k == n:
                solution()
            else:
                if f + Cm * (n-k) < fmin:
                    trial(k+1)  
            visited[v] = False
            f = f - c[x[k-1]][c[k]]

n, c = input()
print(n, c)
Cm = 1e9
for i in range(n):
    for j in range(n):
        if i != j and c[i][j] < Cm:
            Cm = c[i][j]
            
visited = [False for v in range(n)]
f = 0
fmin = 1e9
x = [0 for i in range(n)]

x[0] = 0
visited[0] = True
trial(1)
print(fmin)