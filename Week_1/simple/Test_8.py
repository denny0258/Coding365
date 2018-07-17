import math


def main():
    Data = {
        183: 0,
        383: 0,
        983: 0
    }
    F = [(0.08, 0.07, 0.06), (0.139, 0.130, 0.108), (0.135, 0.121,
                                                     0.101), (1.128, 1.128, 1.128), (1.483, 1.483, 1.483)]

    for i in range(5):
        Data = Get(int(input()), Data, F[i])
    temp = list()
    for k, v in Data.items():
        temp.append((v-k, k))
    temp.sort()
    if temp[2][0] < 0:
        print("{}\n{}".format(temp[2][1], temp[2][1]))
    else:
        for i in temp:
            if i[0] > 0:
                print("{}\n{:.0f}".format(i[1], i[0] + i[1]))
                break


def Get(M, D, F):
    D[183] = D.get(183, 0) + M * F[0]
    D[383] = D.get(383, 0) + M * F[1]
    D[983] = D.get(983, 0) + M * F[2]
    return D


# =========================================
if __name__ == "__main__":
    main()
