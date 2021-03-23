#!/usr/bin/python


# @package gapalib
# Gapalib is mathematical library for GazorPazorp calculator.
#
# This math library contains basic mathematical function.
#


##
# @brief Function to add two numbers
#
# @param add1 First addend
# @param add2 Second addend
#
# @return Sum of add1 and add2
@staticmethod
def add(add1, add2):
    return add1 + add2

##
# @brief Function to substract one number from another
#
# @param minuend Number we substract from
# @param subtrahend Number we substract
#
# @return difference of minuend and subtrahend
@staticmethod
def sub(minuend, subtrahend):
    return minuend - subtrahend

##
# @brief Function to multiply two numbers
#
# @param a First number to be multiplied
# @param b Second number to be multiplied
#
# @return Product of a and b
@staticmethod
def mul(a, b):
    return a * b

##
# @brief Function to divide two numbers
#
# @param a Dividend
# @param b Divisor
#
# @return Quotient of two numbers
@staticmethod
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
@staticmethod
def factorial(a):
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
# @param a Base (number)
# @param exp Exponent
#
# @return power
@staticmethod
def power(a, exp):
    return pow(a, exp)

##
# @brief Function to compute root
#
# @param deegree Root degree
# @param radicand Root radicand
#
# @return power
@staticmethod
def root(degree, radicand):
    if degree % 2 == 1 and radicand < 0:
        raise ValueError("Error - even root of a negative radicant")
    if radicand == 0:
        raise ValueError("Error - radicant can't be zero")

    root = pow(radicand, 1/degree)
    return root
