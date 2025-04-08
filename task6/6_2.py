import math


def build_phi(data):
    result = []
    for w in data:
        if w < -53 or w > 32:
            result.append(math.ceil(w / 2))
    return result


def build_p(data):
    result = []
    for w in data:
        if -15 <= w < 42:
            result.append(w % 3)
    return result


def build_psi(phi):
    result = []
    for f in phi:
        if (f > -84) ^ (f <= 27):
            result.append(math.ceil(f / 7))
    return result


def main(omega):
    phi = build_phi(omega)
    p = build_p(omega)
    theta = set(p).union(phi)
    psi = build_psi(phi)
    result = len(theta.union(psi)) + sum(psi)
    return result
