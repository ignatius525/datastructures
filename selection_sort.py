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
    
selection_sort(a)
print(a)