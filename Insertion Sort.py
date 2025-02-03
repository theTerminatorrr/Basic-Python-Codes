
def insertion(array):

    for i in range(1, len(array)):
        val = array[i]
        j = i

        while j > 0 and array[j - 1] > val:
            array[j] = array[j - 1]
            j -= 1

        array[j] = val

array = list(map(int, input("Enter the Array elements : ").split()))

insertion(array)

print("Sorted array:", array)

