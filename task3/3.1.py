def main(n, a, b):
    s = 0
    for j in range(1, b+1):
        for i in range(1, a+1):
            for c in range(1, n+1):
                s += i**7-(54*j*j+63+c)**3
    return s
