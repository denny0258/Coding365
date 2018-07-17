
def stack():
    Data = list()
    while True:
        cho = input()
        cho = cho.split(" ")
        if cho[0] == "1":
            if len(Data) > 4:
                print("FULL")
                break
            else:
                Data.append(cho[1])
        elif cho[0] == "2":
            if len(Data) == 0:
                print("EMPTY")
                break
            else:
                Data.pop()
        elif cho[0] == "3":
            print(" ".join(Data))
            break
        
def circular_queue():
    Data = list()
    while True:
        cho = input()
        cho = cho.split(" ")
        if cho[0] == "1":
            if len(Data) > 3:
                print("FULL")
                break
            else:
                Data =[cho[1]] +  Data 
        elif cho[0] == "2":
            if len(Data) == 0:
                print("EMPTY")
                break
            else:
                Data.pop()
        elif cho[0] == "3":
            st = ""
            for i in range(len(Data)):
                st+=Data.pop() + " "
            print(st)
            break

# ========================================
def main():
    cho_m = input()
    cho_m=cho_m.strip()
    if cho_m == "1":
        stack()
    elif cho_m == "2":
        circular_queue()

# =========================================
if __name__ == "__main__":
    main()