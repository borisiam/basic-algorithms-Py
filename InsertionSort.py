
def insertion_sort(array):

    for i in range(len(array)):

        j = i

        while j > 0 and array[j-1] > array[j]:
            swap(array, j, j-1)

            j -=1

    return array


def swap(array, i, j):
    arrayI = array[i]
    array[i] = array[j]
    array[j] = arrayI

    return array

a = [0,30,350,606,22,0,3,5,7,8]

insertion_sort(a)

print(a)