#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    res = 0
    operator = "+-*/"
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif c not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if c == '+':
            res = add(a, b)
        elif c == '-':
            res = sub(a, b)
        elif c == '*':
            res = mul(a, b)
        else:
            res = div(a, b)
        print("{} {} {} = {}".format(a, c, b, res)) 
