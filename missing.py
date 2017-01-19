
"""
	 presented with two arrays of positive intergers, prints the extra number in one array
	 Args:
	 	list1 and list2

	 Return:
	 	difference between list1 and list2

"""
def find_missing(list1,list2):
	if isinstance(list1, list) and isinstance(list2, list):
		"""using symetrical difference/disjunctive union"""
		diff = set(list1)^set(list2)

		if diff:
			return diff.pop()
		else:
			return 0









