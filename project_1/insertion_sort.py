def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = cur

check = 1
a = []
while check > 0:
    val = input("Enter elements of list: ")
    if val == "":
        check = -1
    else:
        toAdd = int(val)
        a.append(toAdd)
    print(a)
    
insertion_sort(a)
print(a)
