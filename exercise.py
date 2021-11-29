import distribution.continuous
import variate


class LCG:

    def __init__(self):
        self.last_checked = 0
        _, self._results, _ = variate.lcg(modulus=100, multiplier=17, increment=43, seed=23, times=101)

    def retrieve_from_lcg(self):
        self.last_checked += 1
        return self._results[self.last_checked - 1]

    @property
    def results(self):
        return self._results


lcg = LCG()

print(lcg.results)

for _ in range(10):
    x, y = distribution.continuous.normal(12, 2, lcg.retrieve_from_lcg)
    f1, f2 = float('%.2f' % x), float('%.2f' % y)
    s1, s2 = str(f1), str(f2)
    s1 = s1.replace('.', ',')
    s2 = s2.replace('.', ',')
    print(s1)
    print(s2)
