from serialsearch import *

def main1():
	list1 = ['E', 'B', 'E', 'F', 'A', 'F']
	list2 = ['E', 'B', 'E', 'F', 'A', 'F']
	first=5
	size=1
	target='F'
	i = 0
	while i == 0:

		target1 = search(list1,first,size,target)
		# print (target1)
		target2 = search(list2,first,size,target)
		# print(target2)

		if target1 == target2:
			print('Two lists are strictly identical')
		else: 
			print('Two lists are not strictly identical')
		i=+1
	print (list1)
	print (list2)

main1()

def main2():

	list1 = ['E', 'B', 'E', 'F', 'A', 'C']
	list2 = ['E', 'B', 'E', 'F', 'A', 'F']
	first=5
	size=1
	target='C'
	i = 0
	while i == 0:

		target1 = search(list1,first,size,target)
		# print (target1)
		target2 = search(list2,first,size,target)
		# print(target2)

		if target1 == target2:
			print('Two lists are strictly identical')
		else: 
			print('Two lists are not strictly identical')
		i=+1
	print (list1)
	print (list2)

main2()

def main3():
	list1 = ['E', 'B', 'E', 'F', 'A', 'F', 'C']
	list2 = ['E', 'B', 'E', 'F', 'A', 'F']
	first=6
	size=1
	target='C'
	i = 0
	while i == 0:

		target1 = search(list1,first,size,target)
		# print (target1)
		target2 = search(list2,first,size,target)
		# print(target2)

		if target1 == target2:
			print('Two lists are strictly identical')
		else: 
			print('Two lists are not strictly identical')
		i=+1
	print (list1)
	print (list2)

main3()