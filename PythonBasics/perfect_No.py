def Perfect_Number(num):
    Sum = 0
    for i in range(1, num):
        if (num % i == 0):
            Sum = Sum + i
    return Sum


if __name__ == "__main__":
    print("Please Enter any number: ")
    num = int(input())
    output = Perfect_Number(num)

    if (num == output):
        print(num, " is a Perfect Number")
    else:
        print(num, " is not a Perfect Number")
