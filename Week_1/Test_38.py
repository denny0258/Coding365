def main():
    T_Data = dict()
    S_Data = dict()



    temp = input().strip().replace(",", "")
    S_Data[chr(90-len(temp)+1)] = temp
    # =========================
    for i in range(90-len(temp)+2,91):
        S_Data[chr(i)] = input().strip().replace(",", "")
    
    T_Data["A"] = input().strip().replace(",", "")

    for i in range(66,65+len(T_Data["A"])):
        T_Data[chr(i)] = input().strip().replace(",", "")


    # =========================
    i = 0
    Out = list()
    t = list()
    while len(Out) != len(T_Data):
        Data = dict()
        for k, v in S_Data.items():
            if k not in t and v[i] not in t:
                Data[v[i]] = Data.get(v[i], []) + [k]
        if Data != dict():
            Out, t = get(Data, T_Data, Out, t)
        i += 1
    Out.sort()
    for i in Out:
        print("{}->{}".format(i[0], i[1]))


def get(Data, T_Data, Out, t):
    for k, v in Data.items():
        if len(v) > 1:
            temp = list()
            for i in v:
                temp.append((T_Data[k].find(i), i))
            temp.sort()
            for i in range(len(temp)):
                if temp[i][1] not in t:
                    Out.append((temp[i][1], k))
                    t.append(temp[i][1])
                    break
        else:
            Out.append((v[0], k))
            t.append(v[0])
        t.append(k)
    return Out, t


# =========================================
if __name__ == "__main__":
    main()
