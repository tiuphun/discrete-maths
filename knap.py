

def solution():
    
def trial(k):
    for v in range((b-w)/a[k], 0):
        x[k] = v
        w = w + a[k]*x[k]
        f = f + c[k]*x[k]
        if k == n:
            solution()
        else:
            g = f + (b-w) * (c[k+1]/a[k+1])
            if g > f_max:
                trial(k+1)
        w = w - a[k]*x[k]
        f = f - c[k]*x[k]
        