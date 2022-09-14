def quotient_remainder(n, m):
    q = n//m
    r = n % m
    return [q, r]


if __name__ == "__main__":
    print("Enter the dividend number:")
    n = int(input())
    print("Enter the Divisor:")
    m = int(input())
    output = quotient_remainder(n, m)
    n, m = output
    print("Reminder is ", n)
    print("Quotient is ", m)
