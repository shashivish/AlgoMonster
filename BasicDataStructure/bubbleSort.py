def bubble_sort(unsorted_list) -> list :
	for i in reversed(range(len(unsorted_list))):
		swapped = False 
		for j in range(i):
			if unsorted_list[j] > unsorted_list[j+1]:
				unsorted_list[j] , unsorted_list[j+1] = unsorted_list[j+1] ,unsorted_list[j]		
				swapped = True

		if not swapped : 
			return unsorted_list 		

	return unsorted_list			

if __name__ ==  '__main__' :
	
	unsorted_list = [4,3,6,1,8,0]
	sorted_list = bubble_sort(unsorted_list)
	print(sorted_list)