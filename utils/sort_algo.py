def sort_algo(obj_list, criterion):
	"""
	define the sorting algorithm
	:param obj_list:
	:param criterion:
	:return:
	"""
	flag = False
	while not flag:
		flag = True
		for i in range(len(obj_list) - 1):
			if criterion(obj_list[i], obj_list[i + 1]):
				continue
			obj_list[i], obj_list[i + 1] = obj_list[i + 1], obj_list[i]
			flag = False
	return obj_list
