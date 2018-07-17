# ========================================
def main():
    temp = {
        "Name": None,
        "Id": None,
        "Total": None,
        "Average":None 
    }
    temp["Name"]= input()
    temp["Id"]= input()
    k = 0
    for i in range(3):
        k += int(input())

    temp["Total"] = str(k)
    temp["Average"] = str(int(k / 3))
    
    for k, v in temp.items():
        print(k+":"+v)

# =========================================
if __name__ == "__main__":
    main()