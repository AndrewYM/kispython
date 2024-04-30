def main(y, x, z):
    n = len(y)
    res = 0
    i = n
    while i > 0:
        res += (y[i-1]**2+63*z[n-i]**3+37*x[n-i])**3
        i -= 1
    return 48*res
