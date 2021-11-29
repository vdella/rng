from scipy.stats import uniform as u


def midsquare(seed: int, times: int = 1):
    int_result = list()
    float_result = list()

    if 0 < seed < 9999:  # Checks if it has 4 digits.

        for i in range(times):
            written_square = str(seed * seed)

            if len(written_square) < 8:
                # If it does not have 8 digits at squared form,
                # we'll need to append the needed digits as zeros
                # at the left side.
                zeros_at_left = 8 - len(written_square)
                written_square.zfill(zeros_at_left)

            next_seed = written_square[2:5 + 1]  # Takes the 4 middle digits.
            int_result.append(int(next_seed))
            float_result.append(float('0.{}'.format(next_seed)))
            seed = int(next_seed)

    return int_result, float_result


def lcg(modulus: int,
        multiplier: int,
        increment: int,
        seed: int,
        times: int):
    int_result = list()
    float_result = list()
    period, initial_seed = 0, seed

    for i in range(times):
        int_result.append(seed)
        seed = (multiplier * seed + increment) % modulus
        float_result.append(seed / modulus)

        if initial_seed == seed:
            period = i + 1

    return int_result, float_result, period


def uniform():
    return u.rvs(0)


if __name__ == '__main__':
    print(lcg(16, 5, 3, 7, 7)[1])
    print(lcg(modulus=100, multiplier=17, increment=43, seed=23, times=101)[1])
