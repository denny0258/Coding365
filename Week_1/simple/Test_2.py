import math
def main():
    
    a = float(input())
    b = float(input())
    c = float(input())

    print("{:.1f}".format((-b+math.sqrt(b*b-4*a*c))/(2*a)))
    print("{:.1f}".format((-b-math.sqrt(b*b-4*a*c))/(2*a)))



# =========================================
if __name__ == "__main__":
    main()