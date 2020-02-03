import time
import random

def selection_sort(arr):
    for k in range(len(arr)):
        min = k
        j = k 
        while j < len(arr)-1:
            j +=1
            cur = j
            if (arr[cur]<arr[min]):
                min = cur
        if min != k:
            arr[k], arr[min] = arr[min], arr[k]
        print(arr)

def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = cur
        print(arr)

a = [8,7,6,5,4,3,2,1]
b = [8,7,6,5,4,3,2,1]

insertion_sort(a)
print(a)
print("")
selection_sort(b)
print(b)