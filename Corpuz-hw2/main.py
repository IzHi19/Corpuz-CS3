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
def bubble_sort(unsortedArr):
    start = time.perf_counter()
    for i in range(0,len(unsortedArr)):
        for j in range(i,len(unsortedArr)):
            if unsortedArr[i]>unsortedArr[j]:
                temp = unsortedArr[i]
                unsortedArr[i] = unsortedArr[j]
                unsortedArr[j] = temp


    return start
    for b in range(0,10):
        print(unsortedArr[b])

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
    print(f"bubble sort took {bubble_sort(unsortCopy)} seconds to sort")
    for i in range(0,10):
        print(unsortCopy[i])



if __name__ == '__main__':
    unsortedArr = buildArr()
    sortTimer(unsortedArr)
