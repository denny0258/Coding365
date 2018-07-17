def priority(op):
    return 1 if op in "+-" else 2 if op in "*/" else 3 if op == "^" else 0

def toPostfix(infix):
    def procOpt(c, stack, output):
        if stack == "" or priority(stack[-1]) < priority(c):
            return (stack + c, output)
        else:
            return procOpt(c, stack[0:-1], output + stack[-1])

    def procPhs(stack, output):
        if stack[-1] == '(':
            return (stack[0:-1], output)
        else:
            return procPhs(stack[0:-1], output + stack[-1])

    def procExpr(expr, stack="", output=""):
        if expr == "":
            return output + stack[::-1]
        elif expr[0] == '(':
            return procExpr(expr[1:], stack + expr[0], output)
        elif expr[0] in "+-*/^":
            return procExpr(expr[1:], *procOpt(expr[0], stack, output))
        elif expr[0] == ')':
            return procExpr(expr[1:], *procPhs(stack, output))
        else:
            return procExpr(expr[1:], stack, output + expr[0])

    output = procExpr(infix).replace(" ","")
    return output


def main():
    infix = input()
    print(toPostfix(infix))

# =========================================
if __name__ == "__main__":
    main()
