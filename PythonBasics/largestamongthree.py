def largestno(a, b, c):
    if a > b:
        if b > c:
            return a
        else:
            if c > a:
                return c
            else:
                return a
    else:
        if b > c:
            return b
        else:
            return c


if __name__ == "__main__":
    print("Enter three Numbers: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
large = largestno(num1, num2, num3)
print("\nLargest Number =", large)
