def main():
    while True:
        Data = input() 
        if Data == "-1":
            break
        elif Data == "0":
            pass
        else:
            print(str(bin(C(int(Data, 2))))[2:].zfill(11))


def C(m):
    i = 0
    for s in range(m+1):
        while True:
            if s == 0 or s == 1:
                break
            i += 1
            if s % 2 == 0:
                s /= 2
            else:
                s = (s + 1) / 2
    return i


if __name__ == "__main__":
    main()
