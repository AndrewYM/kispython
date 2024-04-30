def main(n, a, b):
    s = 0
    j = 1
    while j <= b:
        i = 1
        while i <= a:
            c = 1
            while c <= n:
                s += i**7 - (54*j*j + 63 + c)**3
                c += 1
            i += 1
        j += 1
    return s
