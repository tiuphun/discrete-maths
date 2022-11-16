# Generate all solutions x1 + x2 + ... + xn = M; given n, M.
[n, M] = [int]
x = [0 for i in range(n+1)]
T = 0

def solution():
    print(x[1:])
def check(v, k):
    if k < n:
        return True
    return T + v == M
def trial(k):
    global T
    for v in range (1, M - T - n+k+1):
        if check(v, k):
            x[k] = v
            T = T + x[k]
            if k == n:
                solution()
            else: 
                trial(k+1)
            T = T - x[k]