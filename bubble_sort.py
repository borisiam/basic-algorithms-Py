
def bubble_sort(array):

    for i in range(len(array)-1):
        for j in range(0, len(array)-1 -i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)

    return array


def swap(array, i, j):
    arrayI = array[i]
    array[i] = array[j]
    array[j] = arrayI

    return array

a = [0,30,350,606,22,0,3,5,7,8]

bubble_sort(a)

print(a)