def main(n, a, b):
    def helper(i, j, c, s):
        if i > a:
            return s
        if j > b:
            return helper(i+1, 1, 1, s)
        if c > n:
            return helper(i, j+1, 1, s)
        s += i**7 - (54*j*j + 63 + c)**3
        return helper(i, j, c+1, s)
    return helper(1, 1, 1, 0)
