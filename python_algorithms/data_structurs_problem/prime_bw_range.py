def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


if __name__ == "__main__":
    starts = 0
    ends = 1000
    lst = prime(starts, ends)
    if len(lst) == 0:
        print("There are no prime numbers in this range")
    else:
        print("The prime numbers in this range are: ", lst)
