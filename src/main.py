import random
import timeit


def main():
    sortingAlgorithms = {
        'bubble sort': 1,
        'merge sort': 2,
        'insertion sort': 3,
        'shell sort': 4,
        'selection sort': 5,
        'standard python sort': 6
    }

    print('Welcome to Python sorting algorithms demonstration\nThis programs allow you to choose a sort algorithm and'
          ' see in how much time a set is sorted')

    j = 1
    while True:
        for i in sortingAlgorithms:
            print(str(j) + ') ' + i)
            j += 1
        choose = input("0) Per uscire\nInserisci l'algoritmo desiderato:")
        if choose == '0' or choose > max(sortingAlgorithms):
            break
        else:
            j = 1
            start_sorting(choose)


def bubbleSort(sample):
    has_swapped = True

    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(sample) - num_of_iterations - 1):
            if sample[i] > sample[i + 1]:
                # Swap
                sample[i], sample[i + 1] = sample[i + 1], sample[i]
                has_swapped = True
        num_of_iterations += 1


def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def mergeSort(sample, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    mergeSort(sample, left_index, middle)
    mergeSort(sample, middle + 1, right_index)
    merge(sample, left_index, right_index, middle)


def insertionSort(sample):

    for index in range(1, len(sample)):
        currentValue = sample[index]
        currentPosition = index

        while currentPosition > 0 and sample[currentPosition - 1] > currentValue:
            sample[currentPosition] = sample[currentPosition - 1]
            currentPosition = currentPosition - 1

        sample[currentPosition] = currentValue


def shellSort(sample):
    # Start with a big gap, then reduce the gap
    n = len(sample)
    gap = int(n / 2)

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = sample[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and sample[j - gap] > temp:
                sample[j] = sample[j - gap]
                j -= gap

                # put temp (the original a[i]) in its correct location
            sample[j] = temp
        gap = int(gap / 2)


def selectionSort(sample):
    # i indicates how many items were sorted
    for i in range(len(sample) - 1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i + 1, len(sample) - 1):
            # Update the min_index if the element at j is lower than it
            if sample[j] < sample[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        sample[i], sample[min_index] = sample[min_index], sample[i]


def start_sorting(choose):
    sample = []
    for i in range(10000):
        sample.append(random.randint(0, 1000000))

    startTime = timeit.default_timer()

    if choose == '1':
        bubbleSort(sample)
    elif choose == '2':
        mergeSort(sample, 0, len(sample) - 1)
    elif choose == '3':
        insertionSort(sample)
    elif choose == '4':
        shellSort(sample)
    elif choose == '5':
        selectionSort(sample)
    else:
        sample.sort()

    print('Tempo di esecuzione: ', timeit.default_timer() - startTime)
    print('\nPrimi 10 valori: ')
    for i in range(10):
        print(sample[i], ' ')
    print('\nUltimi 10 valori: ')
    length = len(sample)
    for i in reversed(range(length - 10, length)):
        print(sample[i], ' ')


if __name__ == '__main__':
    main()
