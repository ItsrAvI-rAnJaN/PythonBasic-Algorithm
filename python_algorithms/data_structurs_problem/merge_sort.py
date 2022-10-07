def merge_sort(a):

    if len(a) > 1:

        mid = len(a) // 2

        left_subarray = a[:mid]

        right_subarray = a[mid:]

        merge_sort(left_subarray)
        merge_sort(right_subarray)

        i = j = k = 0

        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] < right_subarray[j]:
                a[k] = left_subarray[i]
                i += 1
            else:
                a[k] = right_subarray[j]
                j += 1
            k += 1

        while i < len(left_subarray):
            a[k] = left_subarray[i]
            i += 1
            k += 1
        while j < len(right_subarray):
            a[k] = right_subarray[j]
            j += 1
            k += 1


if __name__ == "__main__":

    array = list(
        map(int, input("Enter integer separated by spaces : ").strip().split()))
    print("Array is : ", array)
    merge_sort(array)
    print("Merge sorted array is : ", array)
