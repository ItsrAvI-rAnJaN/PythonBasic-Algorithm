def selection_sort(a):

    for i in range(len(a) - 1):

        minimum = i

        for j in range(i + 1, len(a)):

            if a[j] < a[minimum]:
                minimum = j

        a[i], a[minimum] = a[minimum], a[i]
    return a


if __name__ == "__main__":
    array = list(
        map(int, input("Enter integer separated by spaces : ").strip().split()))
    print("Array is : ", array)
    print("Selection sorted array is : ", selection_sort(array))
