def main(y, x, z):
    n = len(y)
    i = 1

    def calc(i):
        if i > n:
            return 0
        return (
            y[i - 1] ** 2 + 63 * z[n - i] ** 3 + 37 * x[n - i]) ** 3 + calc(
            i + 1)
    return 48 * calc(i)
