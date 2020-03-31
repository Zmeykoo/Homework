intList = int(input("Введіть 4-их значне число:"))
if intList<999:
	print('Error:number is lower than allowed')
elif intList>9999:
	print ('Error:number is larger than allowed')
else:
	uList=list(map(int, str(intList)))
	print('intList =',type(intList))
	print('uList =',type(uList),'\n')
	print ('\nnumb =',uList)

	sum=1
	for nus in uList:
		sum *=int(nus)
	print('Добуток з його цифр:',sum)
	uList.reverse()
	print('Реверсивний порядок:',uList)
	print('Посортаване',sorted(uList))
