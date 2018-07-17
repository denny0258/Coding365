def main():
    while True:
        Data = input() 
        if Data == "-1":
            break
        elif Data == "0":
            pass
        else:
            print(str(bin(C(int(Data, 2))))[2:].zfill(4))


def C(m):
    i = 0
    while True:
        if m == 0 or m == 1:
            break
        i += 1
        if m % 2 == 0:
            m /= 2
        else:
            m = (m + 1) / 2
    return i


if __name__ == "__main__":
    main()
