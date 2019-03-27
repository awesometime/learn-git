[](https://mmbiz.qpic.cn/mmbiz_gif/gsQM61GSzIMLb3kBhQibib6HpVZIdyA3icibU0njhmkHq9cQtYkKrybVIsJkBHuN5XvRubHoOchWia2t2TTg6NMw7dg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)
# https://www.geeksforgeeks.org/radix-sort/
# Python program for implementation of Radix Sort 

# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 

	n = len(arr) 

	# The output array elements that will have sorted arr 
	output = [0] * (n) 

	# initialize count array as 0 
	count = [0] * (10) 

	# Store count of occurrences in count[] 
	for i in range(0, n): 
		index = (arr[i]/exp1) 
		count[ (index)%10 ] += 1

	# Change count[i] so that count[i] now contains actual 
	# position of this digit in output array 
	for i in range(1,10): 
		count[i] += count[i-1] 

	# Build the output array 
	i = n-1
	while i>=0: 
		index = (arr[i]/exp1) 
		output[ count[ (index)%10 ] - 1] = arr[i] 
		count[ (index)%10 ] -= 1
		i -= 1

	# Copying the output array to arr[], 
	# so that arr now contains sorted numbers 
	i = 0
	for i in range(0,len(arr)): 
		arr[i] = output[i] 

# Method to do Radix Sort 
def radixSort(arr): 

	# Find the maximum number to know number of digits 
	max1 = max(arr) 

	# Do counting sort for every digit. Note that instead 
	# of passing digit number, exp is passed. exp is 10^i 
	# where i is current digit number 
	exp = 1
	while max1/exp > 0: 
		countingSort(arr,exp) 
		exp *= 10

# Driver code to test above 
arr = [ 170, 45, 75, 90, 802, 24, 2, 66] 
radixSort(arr) 

for i in range(len(arr)): 
	print(arr[i]), 

# This code is contributed by Mohit Kumra 


# This code is contributed by Mohit Kumra
#         [170, 45, 75, 90, 802, 24, 2, 66]
# //1     [170, 45, 75, 90, 802, 24, 2, 66]
# %10     [0,   5,   5,  0,  2 ,  4, 2,  6]
#         [0,   0,   2,  2,  4,   5, 5,  6]
#           [2, 2, 4, 4, 5, 7, 8, 8, 8, 8]   count
#         [170, 90, 802, 2, 24, 45, 75, 66]   个位sort
# //10
# %10
# [2, 2, 3, 3, 4, 4, 5, 7, 7, 8]    count
# [802, 2, 24, 45, 66, 170, 75, 90]        十位sort
# //100
# %10
# [6, 7, 7, 7, 7, 7, 7, 7, 8, 8]    count
# [2, 24, 45, 66, 75, 90, 170, 802]  百位sort
