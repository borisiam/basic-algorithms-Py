
def quick_sort(array, low, high):

    if low >= high:
        return

    pivot_index = partition(array, low, high)
    quick_sort(array, low, pivot_index - 1)
    quick_sort(array, pivot_index + 1, high)


def partition(array, low, high):

    pivot_index = int((low+high)/2)
    swap(array, pivot_index, high)

    i = low

    for j in range(low, high, 1):
        if array[j] <= array[high]:
            swap(array, i, j)
            i += 1

    swap(array, i, high)

    return i


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    return array


a = [0, 30, 350, 3, 55, 56, 734, 66]
quick_sort(a, 0, 2)
print(a)