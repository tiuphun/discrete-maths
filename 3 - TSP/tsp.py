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
	# compare the current solution with the best solution found so far
	# update if the current solution is better than the best solution
	if f + c[x[n-1]][x[0]] < fmin:
		fmin = f + c[x[n-1]][x[0]]
		#print('update best ',fmin)
		
	
def Try(k): # partial route x[1] - x[2] - . . . - x[k-1] with distance f, x[k] = ?
	global f
	for v in range(n):
		if visited[v] == False:
			x[k] = v
			visited[v] = True
			f = f + c[x[k-1]][x[k]]
			if k == n-1:
				solution()
			else:
				if f + Cm*(n-k) < fmin: # only continue the search this condition happen
					Try(k+1)
					
			visited[v] = False
			f = f - c[x[k-1]][x[k]]			
		
n,c = input()
#print(n,c)	
Cm = 1e9
for i in range(n):
	for j in range(n):
		if i != j and c[i][j] < Cm:
			Cm = c[i][j]			
		
visited = [False for v in range(n)]
f = 0 # accumulated distance of the route under construction
fmin = 1e9 # min distance of the route found
x = [0 for i in range(n)]

x[0] = 0
visited[0] = True
Try(1)
print(fmin)

#need to output the route also!