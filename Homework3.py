import random
import time

array_size = 50000000

def quicksort(array):
if len(array) <= 1:
return array
else:
pivot = array[0]
left = [x for x in array if x < pivot]
right = [x for x in array if x >= pivot]
return quicksort(left) + [pivot] + quicksort(right)

def bubblesort(array):
n = len(array)
for i in range(n):
for j in range(0, n-i-1):
if array[j] > array[j+1]:
array[j], array[j + 1] = array[j + 1], array[j]
return array

start_time = time.time()