#!/usr/bin/python
###################################################################
# Project name: Gazorpazorp calculator
# File: LibMath.py
# Authors: Vilem Gottwald, Pavel Marek
# Description: Library implementing basic mathematical operations
###################################################################


##
# @file LibMath.py
#
# @package gapalib
# Gapalib is mathematical library for GazorPazorp calculator.
#
# This math library contains basic mathematical function.
#

digits = 10
##
# @brief Function to add two numbers
#
# @param a First addend
# @param b Second addend
#
# @return Sum of a and b
def add(a, b):
    return round(a + b, digits)

##
# @brief Function to substract one number from another
#
# @param a Minuend (number we substract from)
# @param b Subtrahend (number we substract)
#
# @return Difference of a and b
def sub(a, b):
    return round(a - b, digits)

##
# @brief Function to multiply two numbers
#
# @param a First factor
# @param b Second factor
#
# @return Product of a and b
def mul(a, b):
    return round(a * b, digits)

##
# @brief Function to divide two numbers
#
# @param a Dividend
# @param b Divisor
#
# @return Quotient of a and b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Error - dividing by zero")
    return round(a / b, digits)

##
# @brief Function to compute factorial
#
# @param a Number, factorial will be computed from
#
# @return Factorial of given number
def fact(a):
    if not isinstance(a, int) or a < 0:
        raise ValueError("Error - number isn't integer or is smaller than 0")
    if a == 0:
        return 1

    result = a
    while a != 1:
        a -= 1
        result *= a
    return result

##
# @brief Function to compute power
#
# @param a Base
# @param exp Exponent
#
# @return Result of the exponentiation
def power(a, exp):
    if not isinstance(exp, int) or exp <= 0:
        raise ValueError("Error - exponent is not a natural number")

    return round(a**exp, digits)

##
# @brief Function to compute root
#
# @param a Radicand
# @param deg Degree
#
# @return Result of the root
def root(a, deg):
    if deg % 2 == 0 and a < 0:
        raise ValueError("Error - even degree of a negative radicant")
    if deg == 0:
        raise ValueError("Error - degree has to be greater than 0")

    negate = False
    if a < 0 and deg % 2 == 1:
        a = -a
        negate = True

    result = round(a**(1/deg), digits)
    return -result if negate else result

##
# @brief Function to compute absolute value of a given number
#
# @param x Number, absolute value will be computed from
#
# @return Absolute Value of given number
def abs(x):
    if x >= 0:
        return x
    if x < 0:
        return -x

##
# @brief Function that checks whether number can be represented as int,
#        if so, returns the number as int, otherwise as float
#
# @param num Number that is checked
#
# @return Number as float or integer, depending on it's value
def check_int(num):
    if num == int(num):
        return int(num)
    else:
        return float(num)

##
# @brief Function that converts string to int or float depending on its value
#
# @param n_str String that will be converted
#
# @return Float or string, depending on the content of string
def str_to_num(n_str):
    if float(n_str) == int(n_str):
        return int(n_str)
    else:
        return float(n_str)



##
# @brief Function that separates string containing mathematical expression into individual items
#
# @param n_str String that will be separatend
#
# @return List containing expression items
def parse_expr(expression):
    operators_l = ["!", "^", "√", "*", "/", "+", "-"]
    separated = list()
    number = True
    num_str = ""

    for char in expression:
        for op in operators_l:
            if char == op:
                number = False
                break

        if number:
            num_str += char
        else:
            if num_str != "":
                separated.append(num_str)
                num_str = ""
            separated.append(op)
            number =  True
    if num_str != "":
            separated.append(num_str)

    return separated

##
# @brief Function that solves parsed mathematical expression and returns result
#
# @param n_str Mathematical expression to be solved (as a list of items)
#
# @return Result of the expression
def solve_expr(expression):
    operators = [["!"], ["^", "√"], ["*", "/"], ["+", "-"]]
    parsed_expr = parse_expr(expression)
    for op_group in operators:
        i = 0
        while i < len(parsed_expr):
            if parsed_expr[i] in op_group:

                if parsed_expr[i] == "!":
                    operand = str_to_num(parsed_expr[i - 1])
                    parsed_expr[i - 1] = (fact(operand))
                    del parsed_expr[i]
                    i -= 1

                elif parsed_expr[i] == "^":
                    base = str_to_num(parsed_expr[i - 1])
                    exponent = str_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (power(base, exponent))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "√":
                    degree = str_to_num(parsed_expr[i - 1])
                    base = str_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (root(base, degree))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "*":
                    operand1 = str_to_num(parsed_expr[i - 1])
                    operand2 = str_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (mul(operand1, operand2))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "/":
                    operand1 = str_to_num(parsed_expr[i - 1])
                    operand2 = str_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (div(operand1, operand2))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "+":
                    operand1 = str_to_num(parsed_expr[i - 1])
                    operand2 = str_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (add(operand1, operand2))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2

                elif parsed_expr[i] == "-":
                    operand1 = str_to_num(parsed_expr[i - 1])
                    operand2 = str_to_num(parsed_expr[i + 1])
                    parsed_expr[i - 1] = (sub(operand1, operand2))
                    del parsed_expr[i + 1]
                    del parsed_expr[i]
                    i -= 2
            i += 1
    return parsed_expr[0]
# End of file LibMath.py
