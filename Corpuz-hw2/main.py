#Programmer: Isabella Corpuz
#Hw-2: timer for different sorting algorithms

import random
import time


def buildArr() -> list:
    newArr = []
    for i in range (10):
    # for i in range(10):
        newArr.append(random.randint(1,10000))
    return newArr

def builtInSort(unsortedArr):
    unsortedCopy = unsortedArr[:]

    return sorted(unsortedCopy)

#done
def bubble_sort(unsortedArr):

    unsortedCopy = unsortedArr[:]
    for i in range(0,len(unsortedCopy)):
        for j in range(i,len(unsortedCopy)):
            if unsortedCopy[i]>unsortedCopy[j]:
                temp = unsortedCopy[i]
                unsortedCopy[i] = unsortedCopy[j]
                unsortedCopy[j] = temp


    return unsortedCopy

#done
def select_sort(unsortedArr):
    #first element is deemed the smallest, walk through the list and swap as needed
    unsortedCopy = unsortedArr[:]
    for i in range(0,len(unsortedCopy)):
        smallest = i
        for j in range(i+1,len(unsortedCopy)):
            if (unsortedCopy[j]< unsortedCopy[smallest]):
                smallest = j

        temp = unsortedCopy[i]
        unsortedCopy[i] = unsortedCopy[smallest]
        unsortedCopy[smallest] = temp

    return unsortedCopy

#done
def quick_sort(unsortedArr):
    unsortedCopy = unsortedArr[:]
    sortedArr = []
    for i in range(0,len(unsortedCopy)):
        toAdd = min(unsortedCopy)
        sortedArr.append(toAdd)
        unsortedCopy.remove(toAdd)

    return sortedArr

#done
def insert_sort(unsortedArr):
    unsortedCopy = unsortedArr[:]
    for i in range(1,len(unsortedCopy)):
        smallest = i
        j = i - 1
        while j >= 0 and unsortedCopy[j] > unsortedCopy[smallest]:
            unsortedCopy[j+1] = unsortedCopy[j]
            j-=1
        unsortedCopy[j+1] = unsortedCopy[i]

    return unsortedCopy
def merge_sort(unsortedArr):
    
    begin = unsortedArr(min(unsortedArr))
    end = unsortedArr.index(max(unsortedArr))
    mid = len(unsortedArr) // 2

def merge(unsortedArr, beg,mid,end):
    leftside = []
    rightsize = []

    for i in range (beg,mid):
        leftside.append(unsortedArr[i])

    for i in range(mid+1,end):
        rightside.append(unsortedArr[i])

def sortTimer(unsortedArr):

    unsortCopy = unsortedArr[:]

    #unsorted list
    print("UnsortedArr: ")
    for i in range(0, 10):
        print(unsortCopy[i])

    print(" ")

    #built-in alg
    builtIn_start = time.perf_counter()
    builtInSorted = builtInSort(unsortCopy)
    builtIn_end = time.perf_counter()

    print(f"Python built-in sort took: {builtIn_end - builtIn_start} seconds")

    for i in range(0, 10):
        print(builtInSorted[i])

    print(" ")


    #bubble
    bubble_start = time.perf_counter()
    bubble_sorted = bubble_sort(unsortCopy)
    bubble_end = time.perf_counter()

    print(f"Bubble sort took: {bubble_end - bubble_start} seconds")

    for i in range(0,10):
        print(bubble_sorted[i])

    print(" ")

    # quick
    quick_start = time.perf_counter()
    quick_sorted = quick_sort(unsortCopy)
    quick_end = time.perf_counter()

    print(f"Quick sort took: {quick_end - quick_start} seconds")
    for i in range(0, 10):
        print(quick_sorted[i])

    print(" ")

    #select
    select_start = time.perf_counter()
    ss_sorted = select_sort(unsortCopy)
    select_end = time.perf_counter()

    print(f"Select sort took: {select_end - select_start} seconds")


    for i in range(0,10):
        print(ss_sorted[i])

    print(" ")

    #insert
    insert_start = time.perf_counter()
    insert_sorted = insert_sort(unsortCopy)
    insert_end = time.perf_counter()

    print(f"Insert sort took: {insert_end - insert_start} seconds")

    for i in range(0, 10):
        print(insert_sorted[i])

if __name__ == '__main__':
    unsortedArr = buildArr()
    sortTimer(unsortedArr)
