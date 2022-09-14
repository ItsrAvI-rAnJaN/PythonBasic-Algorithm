def fibonacci_series(m):
    b = 1
    c = 0
    i = 1
    while i <= n:
        if i == 1:
            c = 0
        elif i == 2 or i == 3:
            c = 1
        else:
            a = b
            b = c
            c = a+b
        if i == n:
            print(c)
        else:
            print(c, end=" ")
        i = i+1


if __name__ == "__main__":
    print("Enter the Value of n: ", end="")
    n = int(input())

    print("\nFirst", n, "Terms of Fibonacci Series are:")
    fibonacci_series(n)
