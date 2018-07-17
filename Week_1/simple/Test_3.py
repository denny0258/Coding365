import math
def main():
    a = float(input())
    b = float(input())

    print("Sum:{:.2f}".format(a+b))
    print("Difference:{:.2f}".format(abs(a-b)))
    print("Product:{:.2f}".format(a * b))
    print("Quotient:{:.2f}".format(math.floor((a/b)*100)/100))

# =========================================
if __name__ == "__main__":
    main()