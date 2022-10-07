def binarySearch(array, x, smaller, greater):

    while smaller <= greater:

        mid = smaller + (greater - smaller)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            smaller = mid + 1

        else:
            greater = mid - 1

    return -1


if __name__ == "__main__":
    array = ["David", "Dave", "Tuskin", "Rampage"]
    x = "Dave"

    result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Element Not found")
