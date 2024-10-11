# Arithmetic Operators

# Task
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
# 1. The first line contains the sum of the two numbers.
# 2. The second line contains the difference of the two numbers (first - second).
# 3. The third line contains the product of the two numbers.


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    abSum = a + b
    abDiff = a - b
    abProd = a * b
    
    print(abSum)
    print(abDiff)
    print(abProd)
