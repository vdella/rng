import variate
from functools import reduce
from math import log, e


def bernoulli(p):
    return 1 if variate.uniform() <= p else 0


def uniform(a, b):
    return a + (b - a + 1) * variate.uniform()


def binomial(t, p):
    return reduce(lambda a, b: a + b, [bernoulli(p) for _ in range(t)])


def geometric(p):
    return log(variate.uniform()) / log(1 - p)


def negative_binomial(s, p):
    return reduce(lambda a, b: a + b, [geometric(p) for _ in range(s)])


def poisson(power):
    a, b, i = e**(-power), 1, 0

    while b >= a:
        b = b * variate.uniform()
        i += 1

    return b, i


if __name__ == '__main__':
    print(poisson(0.2))
    print(uniform(10, 50))
