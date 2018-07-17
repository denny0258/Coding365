def main():
    while True:
        Data = input()
        if Data == "-1":
            break
        elif Data == "0":
            pass
        else:
            Data = Data.split(" ")
            print(G(int(Data[0]),int(Data[1])))


def G(m, k, out=""):
    if m == 1:
        return out + str(k)
    elif k < 2**(m - 1):
        return out + "0" + G(m - 1, k)
    elif k >= 2**(m - 1):
        return out + "1" + G(m - 1, 2 ** m - 1 - k)


if __name__ == "__main__":
    main()
