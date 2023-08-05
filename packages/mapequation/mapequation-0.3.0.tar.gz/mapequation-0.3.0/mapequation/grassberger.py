import numpy as np


def entropy_function(Gn):
    def entropy(x):
        return Gn[np.array(x).astype(int)]

    return entropy


def coefficients(n):
    gamma = np.euler_gamma  # euler mascheroni constant

    if n % 2 == 0:
        Gn = np.zeros(n + 1)
    else:
        Gn = np.zeros(n + 2)

    Gn[1] = -gamma - np.log(2)
    Gn[2] = 2.0 - gamma - np.log(2)

    i = 3
    while i <= n:
        Gn[i] = Gn[i - 1]
        Gn[i + 1] = Gn[i - 1] + 2.0 / i
        i += 2

    return Gn
