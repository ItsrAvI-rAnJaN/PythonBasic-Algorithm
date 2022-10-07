def insertion_sort(list1):
    for i in range(1, len(list1)):
        temp = list1[i]
        j = i - 1
        while (j >= 0 and temp < list1[j]):
            list1[j + 1] = list1[j]
            j = j - 1
        list1[j + 1] = temp
    return list1


if __name__ == "__main__":
    list1 = input('Enter the list of numbers sepated by space: ').split()
    list1 = [int(x) for x in list1]
    output = insertion_sort(list1)
    print('Sorted list: ', end='')
    print(output)
