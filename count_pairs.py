from collections import defaultdict
def count_pairs(lst):
	if lst:
		numbers = defaultdict(int)
		for item in lst:
			numbers[item] +=1
		results = []
		for number, count in numbers.items():
			if count >=2:
				results.append([number, int(count/2)])
		sorted_result = sorted(results, key=lambda x:x[1], reverse = True)
		if sorted_result :
			print(sorted_result)
		else:
			print('There is no pairs in the current list')

def read_numbers(filename):
	numbers_list=[]
	with open (filename, 'r') as file:
		for line in file:
			for item in file :
				item= item.strip()
				if item.isdigit():
					numbers_list.append(item)
	return numbers_list
	

list_of_numbers = read_numbers('text.txt')
count_pairs(list_of_numbers)
count_pairs([5, 10, 2, 10, 5, 7, 9, 10]	)	
# outputs:

# numbers_list=[5, 10, 2, 10, 5, 7, 9, 10]
# line = '5, 10, 2, 10, 5, 7, 9, 10'
# items =[5, 10, 2, 10, 5, 7, 9, 10]


# output:
# lst = [5, 10, 2, 10, 5, 7, 9, 10]		
# numbers ={ 5: 2, 10:3, 2:1,7:1, 9:1}
# pair=1
# result =[[5,1], [10,1]]
