import numpy as np
from functools import cache

if __name__ == "__main__":
    print("Zadejte délku stěny spirály: ", end="")
    L = int(input())
    print("Zadejte sířku mezery mezi stěnami spirály: ", end="")
    D = int(input())

    assert L > 0
    assert D > 0

    S = L*D*3

    buffer = np.zeros((S, S), np.bool_)
    @cache
    def step(l: int):
        buffer[l,         l-(l != 0)*D:S-l] = True
        buffer[l+1:S-l,   S-l-1]            = True
        buffer[S-l-1,     l+1:S-l-1]        = True
        buffer[l+D+1:S-l, l]                = True
        if l < S-D-1:
            return step(l+D+1)
    step(0)

    for x in range(S):
        for y in range(S):
            print("█" if buffer[x, y] else " ", end="")
        print()
