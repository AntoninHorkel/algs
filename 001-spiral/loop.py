import numpy as np

if __name__ == "__main__":
    print("Zadejte délku stěny spirály: ", end="")
    L = int(input())
    print("Zadejte sířku mezery mezi stěnami spirály: ", end="")
    D = int(input())

    assert L > 0
    assert D > 0

    S = L*D*3

    buffer = np.zeros((S, S), np.bool_)
    for l in range(0, S, D+1): # TODO: Optimal range length.
        buffer[l,         l-(l != 0)*D:S-l] = True
        buffer[l+1:S-l,   S-l-1]            = True
        buffer[S-l-1,     l+1:S-l-1]        = True
        buffer[l+D+1:S-l, l]                = True

    for x in range(S):
        for y in range(S):
            print("█" if buffer[x, y] else "#", end="")
        print()
