
def main():
    Temp = dict()
    Data = input()
    Data = Data.split(",")

    for i in range(int(Data[1])):
        k = input()
        k = k.split(",")
        Temp[k[0]] = Temp.get(k[0], []) + [(k[2], k[1])]
        Temp[k[1]] = Temp.get(k[1], []) + [(k[2], k[0])]

    i = ['1']
    index = '1'
    temp_index = None
    to = 0

    while True:
        Temp[index].sort()
        for count in range(len(Temp[index]) + 1):
            try:
                if Temp[index][count][1] not in i:
                    to += int(Temp[index][count][0])
                    i.append(Temp[index][count][1])
                    index = Temp[index][count][1]
                    break
            except:
                if temp_index != Temp[index][0][1]:
                    to += int(Temp[index][0][0])
                    temp_index = index
                    index = Temp[index][0][1]
                elif (Temp[index][0][2] + Temp[index][0][1]) > Temp[temp_index][1][1]:
                    to -= int(Temp[temp_index][0][0])
                    to += int(Temp[temp_index][1][0])
                    index = Temp[temp_index][1][1]

        if len(i) == int(Data[0]):
            break

    print(to)


# =========================================
if __name__ == "__main__":
    main()
