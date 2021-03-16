# Function to add two numbers  
def addition(addend1, addend2): 
    return addend1 + addend2 
  
# Function to subtract two numbers  
def subtraction(minuend, subtrahend): 
    return minuend - subtrahend 
  
# Function to multiply two numbers 
def multiplication(factor1, factor2): 
    return factor1 * factor2 
  
# Function to divide two numbers 
def division(dividend, divisor): 
    if divisor == 0:
        raise Exception("Zero division error")
    return dividend / divisor

# Factorial
def factorial(number):
    if not isinstance(number, int) or number < 0:
        raise Exception("Negative or non-integer factorial error")

    if number == 0:
        return 1

    result = number
    while number != 1:
        number -= 1
        result *= number
    return result

def power(base, exponent):
    return pow(base, exponent)

def square_root(degree, radicand):
    root = pow(radicand, 1/degree)
    return root