def reverse_num(num):
    numlen = len(str(num))
    rev = 0

    for i in range(numlen):
        rev = (num % 10) + (rev*10)
        num = int(num/10)
    return rev


if __name__ == "__main__":
    print("Enter a Number: ", end="")
    num = int(input())
    reverseno = reverse_num(num)
    #rev = reverseno
    print("Reverse of " + str(num) + " is " + str(reverseno))
