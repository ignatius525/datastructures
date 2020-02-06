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
        	temp = arr[k]
        	arr[k] = arr[min]
        	arr[min] = temp   
        

def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = cur

def increasing_order(arr, val):
    for k in range(val):
        arr.append(k)

def decreasing_order(arr,val):
    for k in reversed(range(val)):
        arr.append(k)

def random_order(arr,val):
	for k in range(val):
		arr.append(random.randint(0,val))

def copy_arr(arr1, arr2):
	for k in arr1:
		arr2.append(k)
      
if __name__ == '__main__':

	asc1000_A = list(range(1000))
	asc2500_A = list(range(2500))
	asc5000_A = list(range(5000))
	asc7500_A = list(range(7500))
	asc10000_A = list(range(10000))

	asc1000_B = list(range(1000))
	asc2500_B = list(range(2500))
	asc5000_B = list(range(5000))
	asc7500_B = list(range(7500))
	asc10000_B = list(range(10000))

	des1000_A = list(reversed(range(1000)))
	des2500_A = list(reversed(range(2500)))
	des5000_A = list(reversed(range(5000)))
	des7500_A = list(reversed(range(7500)))
	des10000_A = list(reversed(range(10000)))

	des1000_B = list(reversed(range(1000)))
	des2500_B = list(reversed(range(2500)))
	des5000_B = list(reversed(range(5000)))
	des7500_B = list(reversed(range(7500)))
	des10000_B = list(reversed(range(10000)))

	rand1000_A = []
	random_order(rand1000_A, 1000)

	rand1000_B = []
	copy_arr(rand1000_A, rand1000_B)

	rand2500_A = []
	random_order(rand2500_A, 2500)

	rand2500_B = []
	copy_arr(rand2500_A, rand2500_B)

	rand5000_A = []
	random_order(rand5000_A, 5000)

	rand5000_B = []
	copy_arr(rand5000_A, rand5000_B)

	rand7500_A = []
	random_order(rand7500_A, 7500)

	rand7500_B = []
	copy_arr(rand7500_A, rand7500_B)

	rand10000_A = []
	random_order(rand10000_A, 10000)

	rand10000_B = []
	copy_arr(rand10000_A, rand10000_B)



	start = time.process_time()
	insertion_sort(asc1000_A)
	end = time.process_time()
	print('One Thousand Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(asc1000_B)
	end = time.process_time()
	print('One Thousand Increasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(asc2500_A)
	end = time.process_time()
	print('Two Thousand Five Hundred Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(asc2500_B)
	end = time.process_time()
	print('Two Thousand Five Hundred Increasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(asc5000_A)
	end = time.process_time()
	print('Five Thousand Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(asc5000_B)
	end = time.process_time()
	print('Five Thousand Increasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(asc7500_A)
	end = time.process_time()
	print('Seven Thousand Five Hundred Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(asc7500_B)
	end = time.process_time()
	print('Seven Thousand Five Hundred Increasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(asc10000_A)
	end = time.process_time()
	print('Ten Thousand Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(asc10000_B)
	end = time.process_time()
	print('Ten Thousand Increasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(des1000_A)
	end = time.process_time()
	print('One Thousand Decreasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(des1000_B)
	end = time.process_time()
	print('One Thousand Decreasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(des2500_A)
	end = time.process_time()
	print('Two Thousand Five Hundred Decreasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(des2500_B)
	end = time.process_time()
	print('Two Thousand Five Hundred Decreasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(des5000_A)
	end = time.process_time()
	print('Five Thousand Decreasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(des5000_B)
	end = time.process_time()
	print('Five Thousand Decreasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(des7500_A)
	end = time.process_time()
	print('Seven Thousand Five Hundred Decreasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(des7500_B)
	end = time.process_time()
	print('Seven Thousand Five Hundred Decreasing Selection: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(des10000_A)
	end = time.process_time()
	print('Ten Thousand Decreasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	selection_sort(des10000_B)
	end = time.process_time()
	print('Ten Thousand Decreasing Selection: ' + '{:.6f}'.format(end-start))
	
	
	#print(temporary)
	#insertion_sort(aList)
	#print(temporary)


		

	#insertion_sort(a)
	#print(a)
	#print("")
	#selection_sort(b)
	#print(b)