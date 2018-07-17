def main():
    temp = input()
    temp = [int(i) for i in temp.split(" ")]

    temp.sort()

    if (temp[0] + temp[1]) - temp[2] < 0:
        print("1")
    elif temp[0] == temp[1] == temp[2]:
        print("2")
    elif len(set(temp)) != 3:
        print("3")
    else:
        print("4")



# =========================================
if __name__ == "__main__":
    main()
