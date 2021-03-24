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


##
# @brief Function to add two numbers
#
# @param a First addend
# @param b Second addend
#
# @return Sum of a and b
def add(a, b):
    return a + b

##
# @brief Function to substract one number from another
#
# @param a Minuend (number we substract from)
# @param b Subtrahend (number we substract)
#
# @return Difference of a and b
def sub(a, b):
    return a - b

##
# @brief Function to multiply two numbers
#
# @param a First factor
# @param b Second factor
#
# @return Product of a and b
def mul(a, b):
    return a * b

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
    return a / b

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
    return pow(a, exp)

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
        raise ValueError("Error - degree can't be zero")

    negate = False
    if a < 0 and deg % 2 == 1:
        a = -a
        negate = True

    return -pow(a, 1/deg) if negate else -pow(a, 1/deg)

