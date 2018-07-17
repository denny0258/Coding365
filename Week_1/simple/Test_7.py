import math
def main():
    A = int(input())
    B = int(input())
    C = int(input())

    A = A * 0.8 if A > 30 else A * 0.85 if A > 20 else A * 0.9 if A > 10 else A
    B = B * 0.8 if B > 30 else B * 0.85 if B > 20 else B * 0.95 if B > 10 else B
    C = C * 0.7 if C > 30 else C * 0.8 if C > 20 else C * 0.85 if C > 10 else C

    A *= 380
    B *= 1200
    C *= 180

    print("{:.0f}".format(A+B+C))


# =========================================
if __name__ == "__main__":
    main()
