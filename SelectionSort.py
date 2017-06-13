
def selection_sort(array):

    for i in range(len(array)-1):

        index = i

        for j in range(i +1, len(array), 1):
            if array[j] < array[index]:
                index = j

        if index != i:
            swap(array, index, i)


def swap(array, i, j):
    arrayI = array[i]
    array[i] = array[j]
    array[j] = arrayI

    return array

a = [0,30,350,606,22,0,3,5,7,8]

selection_sort(a)

print(a)