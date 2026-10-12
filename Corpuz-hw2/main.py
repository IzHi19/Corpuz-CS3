#Programmer: Isabella Corpuz
#Hw-2: timer for different sorting algorithms

import random
import time


def buildArr() -> list:
    newArr = []
    # for i in range (10000):
    for i in range(10):
        newArr.append(random.randint(1,10000))
    return newArr

#done
def builtInSort(unsortedArr):

    return sorted(unsortedArr)

#done
def bubble_sort(unsortedArr):
    for i in range(0,len(unsortedArr)):
        for j in range(i,len(unsortedArr)):
            if unsortedArr[i]>unsortedArr[j]:
                temp = unsortedArr[i]
                unsortedArr[i] = unsortedArr[j]
                unsortedArr[j] = temp


    return unsortedArr

#done
def select_sort(unsortedArr):
    #first element is deemed the smallest, walk through the list and swap as needed
    for i in range(0,len(unsortedArr)):
        smallest = i
        for j in range(i+1,len(unsortedArr)):
            if (unsortedArr[j]< unsortedArr[smallest]):
                smallest = j

        temp = unsortedArr[i]
        unsortedArr[i] = unsortedArr[smallest]
        unsortedArr[smallest] = temp

    return unsortedArr

#done
def quick_sort(unsortedArr):
    sortedArr = []
    for i in range(0,len(unsortedArr)):
        toAdd = min(unsortedArr)
        sortedArr.append(toAdd)
        unsortedArr.remove(toAdd)

    return sortedArr

#done
def insert_sort(unsortedArr):
    for i in range(1,len(unsortedArr)):
        smallest = unsortedArr[i]
        j = i - 1
        while j >= 0 and smallest < unsortedArr[j]:
            unsortedArr[j+1] = unsortedArr[j]
            j-=1
        unsortedArr[j+1] = smallest

    return unsortedArr

def merge(left, right):
    temp = []

    j = 0
    i = j

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1

        else:
            temp.append(right[j])
            j += 1

        temp.extend(left[i:])
        temp.extend(right[j:])

        return temp

def merge_sort(unsortedArr):
    step = 1
    length = len(unsortedArr)

    while step < length:
        for i in range(0, length, 2*step):
            left = unsortedArr[i:i + step]
            right = unsortedArr[i+step:i + 2*step]

            merged = merge(left, right)


        for j, val in enumerate(merged):
            unsortedArr[i+j] = val

        step *= 2

        return unsortedArr

def sortTimer(unsortedArr):

    unsortCopy = unsortedArr[:]

    #unsorted list
    print("UnsortedArr: ")
    for i in range(0, 10):
        print(unsortCopy[i])

    print(" ")

    # merge
    merge_list = unsortCopy[:]
    merge_start = time.perf_counter()
    merge_sorted = merge_sort(merge_list)
    merge_end = time.perf_counter()

    print(f"Merge sort took: {merge_end - merge_start} seconds")

    for i in range(0, 10):
        print(merge_sorted[i])

    print(" ")

    #built-in alg
    built = unsortCopy[:]
    builtIn_start = time.perf_counter()
    builtInSorted = builtInSort(built)
    builtIn_end = time.perf_counter()

    print(f"Python built-in sort took: {builtIn_end - builtIn_start} seconds")

    for i in range(0, 10):
        print(builtInSorted[i])

    print(" ")


    #bubble
    bubble = unsortCopy[:]
    bubble_start = time.perf_counter()
    bubble_sorted = bubble_sort(bubble)
    bubble_end = time.perf_counter()

    print(f"Bubble sort took: {bubble_end - bubble_start} seconds")

    for i in range(0,10):
        print(bubble_sorted[i])

    print(" ")

    # quick
    quick = unsortCopy[:]
    quick_start = time.perf_counter()
    quick_sorted = quick_sort(quick)
    quick_end = time.perf_counter()

    print(f"Quick sort took: {quick_end - quick_start} seconds")
    for i in range(0, 10):
        print(quick_sorted[i])

    print(" ")

    #select
    select = unsortCopy[:]
    select_start = time.perf_counter()
    ss_sorted = select_sort(select)
    select_end = time.perf_counter()

    print(f"Select sort took: {select_end - select_start} seconds")


    for i in range(0,10):
        print(ss_sorted[i])

    print(" ")

    #insert
    insert = unsortCopy[:]
    insert_start = time.perf_counter()
    insert_sorted = insert_sort(insert)
    insert_end = time.perf_counter()

    print(f"Insert sort took: {insert_end - insert_start} seconds")

    for i in range(0, 10):
        print(insert_sorted[i])





if __name__ == '__main__':
    unsortedArr = buildArr()
    sortTimer(unsortedArr)
