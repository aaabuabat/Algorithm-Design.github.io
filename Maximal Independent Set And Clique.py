'''
An algorithm that finds the largest independent-set in a
connected graph and another to find the largest clique in a connected graph. 
'''



import copy
import numpy as np
from numpy import concatenate, zeros
from scipy.linalg import toeplitz
Count =0
#================== Maximal Independent Set Function ======================
'''
The Idea here is to take every row and then send it to the ExtractTheConnectedVertic 
function in order check with every element in this row with the other element if there
is any connection or not. After that, the algorithm will compare each set of result from 
each row with other sets to get the maximal or the largest set. 

'''
def MIS(graph): 
    First_list = []
    Templist   = []
    Resultlist = []

    for i in range(len(graph)):
        First_list[:] = []
        First_list.append(i)
        for j in range(len(graph)):
        	
        	if(i==j):
        		continue
        	if (graph[i][j] == 0):
        		First_list.append(j)
        
        Templist=ExtractTheConnectedVertics(graph,First_list)
        if(len(Templist) > len(Resultlist)):
            Resultlist=copy.deepcopy(Templist)
 
    
    return map(lambda x: x + 1, Resultlist)
    
#=============== Extract The Connected Vertics Function =============
def ExtractTheConnectedVertics(graph,First_list):
    global Count
    Templist = []
    Templist.append(First_list[0]) # To improve the algorithm from n^3 + n^2 to just n^3. 
    for z in range(1,len(First_list)):
        for w in range(0,len(First_list)):
        	Count=Count+1
        	if(z>=len(First_list) or w>=len(First_list)):
        		break
        	elif (Count<=len(First_list) and graph[First_list[z]][First_list[w]] == 1):
        		First_list.remove(First_list[z])
        Count=1
    
    Templist=copy.deepcopy(First_list)
    First_list[:] = []
    return Templist
'''
As a matter of fact, the definition of the Independent Set Problem is a subset of V, 
whose elements are pairwise nonadjacent.In contrast, the definition of the Clique Problem
is any complete subgraph of a graph G=(V, E). Thus, we can deduce from these two definitions
that we can solve anyone of these two problems by taking the inverse of the other problem. Therefor,
here we will just replace any element with 1 by zero and replace any element with zero by one,
then we will run the same algorithm that we have use for the Maximal Independent Set. 

'''
def Clique(graph):
    for i in range(len(graph)):
        for j in range(i):
            if (i==j):
                continue
            elif (graph[i][j]==0):
                graph[i][j]=1
                graph[j][i]=1
            else:
                graph[i][j]=0
                graph[j][i]=0
    
    return MIS(graph)

#========================TEST SECTION====================================
graph_test_case1 = np.array ([[0,1,0,1,1,0,0],
                              [1,0,1,1,0,1,0],
                              [0,1,0,1,1,1,1],
                              [1,1,1,0,1,1,0],
                              [1,0,1,1,0,1,0],
                              [0,1,1,1,1,0,0],
                              [0,0,1,0,0,0,0]                  
                              ])

print "The Maximal Independent Set for The Test Case #1 is:",MIS(graph_test_case1)
print "The Largest Clique Set for The Test Case #1 is     :",Clique(graph_test_case1)

graph_test_case2 = np.array([[0,0,1,0,0,1,0,1,1,0,0],
                            [0,0,1,1,1,0,0,1,1,0,1],
                            [1,1,0,1,1,0,1,0,1,0,1],
                            [0,1,1,0,1,0,1,1,1,0,0],
                            [0,1,1,1,0,1,1,0,1,1,0],
                            [1,0,0,0,1,0,1,1,1,1,1],
                            [0,0,1,1,1,1,0,1,1,0,0],
                            [1,1,0,1,0,1,1,0,1,0,1],
                            [1,1,1,1,1,1,1,1,0,0,1],
                            [0,0,0,0,1,1,0,0,0,0,1],
                            [0,1,1,0,0,1,0,1,1,1,0]
                            ])
print "The Maximal Independent Set for The Test Case #2 is:",MIS(graph_test_case2)
print "The Largest Clique Set for The Test Case #2 is     :",Clique(graph_test_case2)



#====== Random (sets) Test Section ================

'''graph=np.random.randint(2, size=(10000));
graph_random_test_case = toeplitz([graph])
print Clique(graph_random_test_case)'''