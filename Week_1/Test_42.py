def C(N):
    if N == 1 or N == 0:
        return 1
    elif N == 2:
        return 2
    else:
        return C(N-1)+C(N-2)+C(N-3)


def main():
    print(C(int(input())))


if __name__ == "__main__":
    main()

