def main(y, x, z):
    res = sum([(y[i-1]**2 + 63*z[len(y)-i]**3 + 37*x[len(
        y)-i])**3 for i in range(1, len(y) + 1)])
    return 48 * res
