def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        search = (first + last) // 2

        if target == arr[search]:
            return search

        elif target < arr[search]:
            last = search - 1

        else:
            first = search + 1

    return None


test = [1,3,5,7,9]
binary_search(test, 9)
print(binary_search(test, 9))
