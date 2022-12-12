# Generating binary sequences of length n (lexicographical order)
n = 3
x = [0 for i in range(n+1)]

def check(v, k):
    return True
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