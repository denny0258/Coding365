import math
def main():
    temp = input()
    temp = [int(i) for i in temp.split(" ") if i ]
    avg = sum(temp) / 5
    e = sum([(i - avg)** 2 for i in temp]) / 5
    b = e ** 0.5
    print("{:.2f}\n{:.2f}\n{:.2f}".format(math.floor((avg)*100)/100,math.floor((e)*100)/100,math.floor((b)*100)/100))

# =========================================
if __name__ == "__main__":
    main()