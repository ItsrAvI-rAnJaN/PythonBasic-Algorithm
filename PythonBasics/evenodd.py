def check_evenodd(num):
    # code logic here
    if num % 2 == 0:
        numtype = "even"
    else:
        numtype = "odd"
    return numtype


if __name__ == "__main__":
    num = int(input('Enter the number: '))
    numtype = check_evenodd(num)
    print(str(num) + ' number is', numtype)
