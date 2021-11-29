import variate
from math import log, e, sqrt, cos, sin, pi


def uniform(a, b, rng=variate.uniform):
    u = rng()
    print(u)
    return a + (b - a) * u


def exponential(beta, rng=variate.uniform):
    u = rng()
    print(u)
    return -beta * log(1 - u)


def gamma(alfa):
    b = (e + alfa) / e
    result = 0

    while result == 0:
        u1 = variate.uniform()
        p = u1 * b

        if p > 1:
            y = - log((b - p) / alfa)
            u2 = variate.uniform()
            result = y if u2 <= e**-y else 0
        else:
            y = p ** (1 / alfa)
            u2 = variate.uniform()
            result = y if u2 <= y**(alfa - 1) else 0
    return result


def weibull(alfa, beta):
    return beta * (- log(1 - variate.uniform()) ** (1 / alfa))


def std_normal(rng=variate.uniform):
    u1 = rng()
    print(u1)
    u2 = rng()
    print(u2)
    b = sqrt(-2 * log(1 - u1))
    return b * cos(2 * pi * u2), b * sin(2 * pi * u2)


def normal(mean, std_deviation, rng=variate.uniform):
    z1, z2 = std_normal(rng=rng)
    print(z1)
    print(z2)
    return mean + std_deviation * z1, mean + std_deviation * z2


def std_triangular(a, b, c, rng=variate.uniform):
    u = rng()
    print(u)
    return a + sqrt(u * (b - a) * (c - a)) if 0 <= u <= (b - a) / (c - a) \
        else c - sqrt((1 - u) * (c - b) * (c - a))


def triangular(m):
    u = variate.uniform()
    return sqrt(m*u) if u <= m else 1 - sqrt((1 - m) * (1 - u))


if __name__ == '__main__':
    # print(std_triangular(0, 1, 2))
    # print(exponential(1))
    print(std_normal())
    print(normal(10, 2))
