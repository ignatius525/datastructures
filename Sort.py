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

	aList = list(reversed(range(50)))

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

	temporary = aList

	rand1000_A = []
	for i in range(1000):
		rand1000_A.append(random.randint(0,1000))

	rand1000_B = []
	for i in range(1000):
		rand1000_B.append(rand1000_A[i])

	rand2500_A = []
	for i in range(2500):
		rand2500_A.append(random.randint(0,2500))
	
	rand2500_B = []
	for i in range(2500):
		rand2500_B.append(rand2500_A[i])
	
	rand5000_A = []
	for i in range(5000):
		rand5000_A.append(random.randint(0,5000))
	
	rand5000_B = []
	for i in range(5000):
		rand5000_B.append(rand5000_A[i])
	
	rand7500_A = []
	for i in range(7500):
		rand7500_A.append(random.randint(0,7500))

	rand7500_B = []
	for i in rand7500_A:
		rand7500_B.append(i)

	rand10000_A = []
	for i in range(10000):
		rand10000_A.append(random.randint(0,10000))

	rand10000_B = []
	for i in range(10000):
		rand10000_B.append(rand10000_A[i])


	start = time.process_time()
	insertion_sort(asc1000_A)
	end = time.process_time()
	print('One Thousand Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(asc2500_A)
	end = time.process_time()
	print('Two Thousand Five Hundred Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(asc5000_A)
	end = time.process_time()
	print('Five Thousand Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(asc7500_A)
	end = time.process_time()
	print('Seven Thousand Five Hundred Increasing Insertion: ' + '{:.6f}'.format(end-start))

	start = time.process_time()
	insertion_sort(asc10000_A)
	end = time.process_time()
	print('Ten Thousand Increasing Insertion: ' + '{:.6f}'.format(end-start))
	
	temparr = []
	increasing_order(temparr,1000)
	print(temparr)

	temporary = []
	decreasing_order(temporary,1000)
	print(temporary)
	#print(temporary)
	#insertion_sort(aList)
	#print(temporary)


		

	#insertion_sort(a)
	#print(a)
	#print("")
	#selection_sort(b)
	#print(b)