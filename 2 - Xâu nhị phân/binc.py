# Generating binary sequences of length n (lexicographical order, with constraints)
n = 5
x = [0 for i in range(n+1)]

# Binary sequences with no consecutive 11's -> modify check()
def check(v, k):
    if k == 1:
        return True
    else:
        return x[k-1] + v <= 1 # forbid the situation that x[k-1] = 1 and v = 1
    
def solution():
    print(x[1:])
    
def trial(k): # explore all values for x[k]
    for v in range(2):
        if check(v, k):
            x[k] = v
            if k == n:
                solution()
            else:
                trial(k+1)
trial(1)
