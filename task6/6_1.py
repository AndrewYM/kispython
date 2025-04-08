import math


def main(omega):
    phi = {math.ceil(w / 2) for w in omega if w not in range(-53, 33)}
    p = {w % 3 for w in omega if ((w < 42) and (w >= -15))}
    theta = p.union(phi)
    psi = {math.ceil(f / 7) for f in phi if ((f > -84) ^ (f <= 27))}
    X = len(theta.union(psi)) + sum(psi)
    return X
