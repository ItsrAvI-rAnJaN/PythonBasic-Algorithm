def swap_num(a, b):
    x = a
    a = b
    b = x
    return [a, b]


if __name__ == "__main__":
    print("Enter the First Number: ", end="")
    a = int(input())
    print("Enter the Second Number: ", end="")
    b = int(input())

    print("\nBefore Swap")
    print("a =", a)
    print("b =", b)
    output = swap_num(a, b)
    a, b = output

    print("\nAfter Swap")
    print("a =", a)
    print("b =", b)
