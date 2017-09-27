import numpy as np
def Seating_Problem(family,table):
	SittingArrangement = np.array( [[0 for x in range(len(table))] for y in range(len(family))]) 
	table=sorted(table, reverse=True)
	for i in range(len(table)):
		for j in range(len(family)):
			if(family[j]>len(table)):
					print "There is no valid arrangement."
					break
			if(family[j]>0 and table[i]>0):
				table[i]=table[i]-1
				family[j]=family[j]-1
				SittingArrangement[j][i]=1

	print SittingArrangement

family=np.array([8,8,5,5,3,2,7])
table=np.array([5,7,2,8,1,6,2,5,3])
Seating_Problem(family,table)