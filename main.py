# With the input of row number, write a program to generate the following pattern:

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

# Here the input is 6.

from math import factorial

def main():
    try:
        rows = input("Enter the number of rows ")
        req_rows = int(rows)
        if req_rows < 0:
            raise ValueError
    except ValueError:
        print("Error occured - Enter a positive integer ")
    else:
        for i in range(req_rows):
            for j in range(i+1):
                print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
            print()
main()