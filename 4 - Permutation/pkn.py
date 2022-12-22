# OK
# Generate permutation of n values
n = 5
x = [0 for i in range(n+1)]
mark = [False for v in range(n+1)]

def check(v, k):
    return mark[v] == False
def solution():
    print(x[1:])
def trial(k):
    for v in range(1, n+1):
        if check(v, k):
            x[k] = v
            mark[v] = True
            if k == n:
                solution()
            else:
                trial(k+1)
            mark[v] = False
trial(1)