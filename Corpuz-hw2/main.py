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
    unsortedCopy = unsortedArr[:]
    smallest = 0
    for i in range(1,len(unsortedCopy)):
        if unsortedCopy[i] < unsortedCopy[smallest]:
            temp = unsortedCopy[i]
            unsortedCopy[i] = unsortedCopy[smallest]
            unsortedCopy[smallest] = temp
            smallest+=1

    return unsortedCopy

def quick_sort(unsortedArr):
    unsortedCopy = unsortedArr[:]
    
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

    print("UnsortedArr: ")
    for i in range(0, 10):
        print(unsortCopy[i])

    print(" ")

    bubble_start = time.perf_counter()
    bubble_sorted = bubble_sort(unsortCopy)
    bubble_end = time.perf_counter()

    print(f"Bubble sort took: {bubble_end - bubble_start} seconds")

    for i in range(0,10):
        print(bubble_sorted[i])

    print(" ")

    select_start = time.perf_counter()
    ss_sorted = select_sort(unsortCopy)
    select_end = time.perf_counter()

    print(f"Select sort took: {select_end - select_start} seconds")

    for i in range(0,10):
        print(ss_sorted[i])

if __name__ == '__main__':
    unsortedArr = buildArr()
    sortTimer(unsortedArr)
