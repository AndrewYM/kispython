def main(y, x, z):
    n = len(y)
    res = 0
    for i in range(1, n + 1):
        res += (y[i-1]**2+63*z[n-i]**3+37*x[n-i])**3
    return 48*res
