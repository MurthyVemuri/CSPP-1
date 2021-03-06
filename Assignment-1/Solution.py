# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and
# returns the factorial of given number.

# This function takes in one number and returns one number.
import math


def factorial(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    return math.factorial(n)


def main():
    data = input()
    for _ in range(int(data)):
        a = input()
        print(factorial(int(a)))

if __name__ == "__main__":
    main()
