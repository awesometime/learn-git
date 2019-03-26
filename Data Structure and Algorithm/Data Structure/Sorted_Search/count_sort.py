
def count_sort(ary):
    max=min=0  # min和max应该用sys.maxint
    for i in ary:
        if i < min:
            min = i
        if i > max:
            max = i 
    count = [0] * (max - min +1)
    for index in ary:
        count[index-min]+=1
    index=0
    for a in range(max-min+1):
        for c in range(count[a]):  # 重点：有多少个就for循环多少次
            ary[index]=a+min
            index+=1
    return ary
    
    
    

# -----------------------------------------------------------------
# https://www.geeksforgeeks.org/counting-sort/
# Python program for counting sort 

# The main function that sort the given string arr[] in 
# alphabetical order 
def countSort(arr): 

	# The output character array that will have sorted arr 
	output = [0 for i in range(256)] 

	# Create a count array to store count of inidividul 
	# characters and initialize count array as 0 
	count = [0 for i in range(256)] 

	# For storing the resulting answer since the 
	# string is immutable 
	ans = ["" for _ in arr] 

	# Store count of each character 
	for i in arr: 
		count[ord(i)] += 1

	# Change count[i] so that count[i] now contains actual 
	# position of this character in output array 
	for i in range(256): 
		count[i] += count[i-1] 

	# Build the output character array 
	for i in range(len(arr)): 
		output[count[ord(arr[i])]-1] = arr[i] 
		count[ord(arr[i])] -= 1

	# Copy the output array to arr, so that arr now 
	# contains sorted characters 
	for i in range(len(arr)): 
		ans[i] = output[i] 
	return ans 

# Driver program to test above function 
arr = "geeksforgeeks"
ans = countSort(arr) 
print "Sorted character array is %s" %("".join(ans)) 

# This code is contributed by Nikhil Kumar Singh 




