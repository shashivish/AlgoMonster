def selection_sort(unsorted_list) -> list : 
	for i in range(len(unsorted_list)) :
		minValue =  i
		for j in range(minValue+1,len(unsorted_list)) :
			if unsorted_list[j] < unsorted_list[minValue]:
				minValue =  j	

		unsorted_list[minValue] , unsorted_list[i] =  unsorted_list[i] , unsorted_list[minValue]  		

	return unsorted_list
if __name__ == '__main__' :
	
	unsorted_list =  [4,3,7,1,9]
	sorted_list = selection_sort(unsorted_list)
	print(sorted_list) 