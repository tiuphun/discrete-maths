# Enumerate k-permutation from n numbers {1, 2, 3, ..., n} s.t. no adjacent values are chosen.
n = 10
k = 4
x = [0 for i in range(k+1)]
cnt = 0

def solution():
    global cnt
    cnt += 1
    print(cnt, ': ', x[1:])
def trial(i):
    for v in range(x[i-1] + 2, n - k + i + 1):
        x[i] = v
        if i == k:
            solution()
        else:
            trial(i+1)
            
x[0] = -1
trial(1) 