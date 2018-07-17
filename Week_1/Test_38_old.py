def main():
    T_Data = dict()
    S_Data = dict()
    for i in ["W", "X", "Y", "Z"]:
        S_Data[i] = input().strip().replace(",", "")
    for i in ["A", "B", "C", "D"]:
        T_Data[i] = input().strip().replace(",", "")
    Data = dict()
    for i in S_Data:
        for k, v in T_Data.items():
            Data[i] = Data.get(i, []) + [((v.find(i) + 1)*1 + (S_Data[i].find(k) + 1)*20, k, i)]

    Data = [k for i in Data.values() for k in i]
    temp = list()
    Data.sort()
    Out_data = list()
    for i in Data:
        if i[1] not in temp and i[2] not in temp:
            Out_data.append((i[2], i[1]))
            temp.append(i[1])
            temp.append(i[2])
    Out_data.sort()
    for i in Out_data:
        print("{}->{}".format(i[0], i[1]))


# =========================================
if __name__ == "__main__":
    main()
