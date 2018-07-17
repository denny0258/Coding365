def main():
    All = input()
    Data = dict()
    for i in range(int(All)-1):
        In_Data = input()
        In_Data = In_Data.split(" ")
        Data[In_Data[1]] = In_Data[0]

    for F in range(int(All) - 1):
        for B in range(F+1, int(All)):
            print("{}-{}-{}".format(F, B, Get(Data, F, B)))

def Get(Data, F, B):
    List_Temp_1 = list()
    List_Temp_2 = list()
    Temp = str(F)
    List_Temp_1.append(Temp)
    while True:
        try:
            List_Temp_1.append(Data[Temp])
            Temp = Data[Temp][0]
        except:
            break
    Temp = str(B)
    List_Temp_2.append(Temp)

    while True:
        try:
            List_Temp_2.append(Data[Temp])
            Temp = Data[Temp][0]
        except:
            break
    Temp = list()
   
    Temp = [i + j for i in range(len(List_Temp_1)) for j in range(len(List_Temp_2)) if List_Temp_1[i] == List_Temp_2[j] and i + j != 0]
    
    try:
        return (min(Temp))
    except:
        return(1)

    # for i in range(len(List_Temp_1)):
    #     for j in range(len(List_Temp_2)):
    #         if List_Temp_1[i] == List_Temp_2[j] and i+j != 0
    #                 Temp.append(i + j)
    


if __name__ == "__main__":
    main()
