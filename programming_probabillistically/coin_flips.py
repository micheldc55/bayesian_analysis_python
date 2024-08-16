import numpy as np
import preliz


def coin_flips(n_trials: int, bias: float, seed: int):
    np.random.seed(seed)

    data = preliz.Binomial(n=1, p=bias).rvs(size=n_trials)

    return data


if __name__ == "__main__":
    head_bias = 0.35
    flips = coin_flips(n_trials=100, bias=head_bias, seed=123)

    print(flips)

    print(f"Number of heads: {flips.sum()}")
    print(f"Number of tails: {(1 - flips).sum()}")
    print(f"Proportion of heads: {flips.mean()} | Real Proportion is: {head_bias}")
