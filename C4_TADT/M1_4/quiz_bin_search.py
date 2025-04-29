#!/usr/bin/env python3

def binary_search(list, key):
	list.sort() # Binary search starts with a sorted list
	left = 0 # The first value of the list
	right = len(list) - 1 # The last value of the list


	while left <= right:
		middle = (left + right) // 2


		if list[middle] == key:
			return middle
		elif list[middle] > key:
			# Add debug statement here
			print("Checking the left side")
			right = middle - 1
		else:
			# Add debug statement here
			print("Checking the right side")
			left = middle + 1
	return -1

print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))