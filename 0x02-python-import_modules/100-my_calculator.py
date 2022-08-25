#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = str(sys.argv[2])

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if op == '+':
            res = add(a, b)
        elif op == '-':
            res = sub(a, b)
        elif op == '*':
            res = mul(a, b)
        elif op == '/':
            res = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(a, op, b, res))
