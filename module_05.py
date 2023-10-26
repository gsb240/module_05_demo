"""
Description: Unit Tests and Functions
Author: Gursimran Singh
Date: 26 October 2023
Usage: Learning about unit test and functions
"""


def add_numbers(number1: int, number2: int) -> int:
    """Returns the sum of two numbers.

    Given two numbers as arguments, this function returns their sum.

    Args:
        number1 (int): The first number to add.
        number2 (int): The second number to add.

    Returns:
        int: The sum of number1 and number2.
    """
    result = number1 + number2
    return result  

def print_sum_of_numbers(number1: int, number2: int) -> None:
    """Prints the sum of two numbers to the console.

    Given two numbers as arguments, this function prints their sum to the console.

    Args:
        number1 (int): The first number to add.
        number2 (int): The second number to add.

    Returns:
        None
    """
    result = number1 + number2
    print(result)
    
print_sum_of_numbers(4, 9)
sum = add_numbers(7,9) #Add sum here
print(sum)

print(print_sum_of_numbers.__doc__)
    