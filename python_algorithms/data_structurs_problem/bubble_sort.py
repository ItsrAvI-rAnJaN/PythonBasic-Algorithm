def bubble_sort(a):
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - i - 1):

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break
    return a


if __name__ == "__main__":
    array = list(
        map(int, input("Enter integer separated by spaces : ").strip().split()))
    print("Array is : ", array)
    print("Bubble sorted array is : ", bubble_sort(array))
