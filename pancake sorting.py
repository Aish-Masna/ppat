# The main function that
# sorts given array
# using flip operations
def pancakeSort(arr, n):
# Start from the complete array and one by one reduce current size by one
	curr_size = n
	while curr_size > 1:
# Find index of the maximum element in arr[0..curr_size-1]
		mi = findMax(arr, curr_size)
# Move the maximum element to end of current array if it's not already at the end
		if mi != curr_size-1:
# To move at the end, first move maximum number to beginning
			flip(arr, mi)

			# Now move the maximum
			# number to end by
			# reversing current array
			flip(arr, curr_size-1)
		curr_size -= 1

# A utility function to
# print an array of size n
def printArray(arr, n):
	for i in range(0,n):
		print ("%d"%( arr[i]),end=" ")

# Driver program
arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)
pancakeSort(arr, n);
print ("Sorted Array ")
printArray(arr,n)