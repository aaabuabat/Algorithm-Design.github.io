'''
 An algorithm that determines whether or not a given undirected graph
contains a cycle.
'''


from collections import defaultdict
import sys  
# Function to create a static variable
def static_num():
    k = -1
    while True:
       k += 1
       yield k

static2L = static_num().next
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices 
        #dictionary to store a graph.
        self.graph = defaultdict(list) 
 
  
   
    def addEdge(self,v,w): #Add edge function.
        self.graph[v].append(w) 
        self.graph[w].append(v) 

    def CycleDetection(self,v,visited,p): 
    	CheckTimeComp = False
        
        visited[v]= True
        for i in self.graph[v]:
        	if  visited[i]==False:
        		static2L()	
        #Here, if the adjacent vertex visited and not parent 
		#of the current vertex; then there is a cycle.
        		if(self.CycleDetection(i,visited,v)):
        			CheckTimeComp = True
        	elif  p!=i:
        		static2L()
        		CheckTimeComp = True
        
        if(CheckTimeComp == True):
        	return True
        else:
        	return False
         
  

    def IsCyclic(self):
    	# This variable will help me to check the time complexity 
    	# by using this static variable "static2L()"
    	CheckTimeComp = False 
    	#Here, we are going to mark all the vertices as not visited. 
        visited= [False for i in range(self.V)]
        for i in range(self.V):
        	static2L()
        	if visited[i] ==False:
        		# Here, we are going to call the function CycleDetection (recursively) above to 
			    # help us to determine whether the graph contains a cycle or not. 
        		if(self.CycleDetection(i,visited,-1)):
        			CheckTimeComp = True
        if(CheckTimeComp == True):
        	return True
        else:
        	return False

# ----------------------TEST SECTION ------------------------------------

g = Graph(8)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 7)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(6, 7)
#=================
g1 = Graph(6)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 3)
g1.addEdge(1, 4)
g1.addEdge(1, 5)

#===============
g2= Graph(15)
g2.addEdge(0, 2)
g2.addEdge(0, 8)
g2.addEdge(0, 10)
g2.addEdge(0, 12)
g2.addEdge(1, 4)
g2.addEdge(1, 5)
g2.addEdge(1, 6)
g2.addEdge(1, 7)
g2.addEdge(1, 8)
g2.addEdge(1, 10)
g2.addEdge(2, 8)
g2.addEdge(2, 11)
g2.addEdge(2, 12)
g2.addEdge(3, 4)
g2.addEdge(3, 6)
g2.addEdge(3, 9)
g2.addEdge(3, 13)
g2.addEdge(3, 14)
g2.addEdge(4, 8)
g2.addEdge(4, 11)
g2.addEdge(4, 14)
g2.addEdge(6, 8)
g2.addEdge(6, 11)
g2.addEdge(7, 9)
g2.addEdge(7, 10)
g2.addEdge(7, 11)
g2.addEdge(8, 10)
g2.addEdge(8, 11)
g2.addEdge(9, 13)
g2.addEdge(10, 14)
g2.addEdge(13, 14)

#=================
print ("The Answer is:")

if g1.IsCyclic():
    print "Yes, the graph contains a cycle"
else :
    print "No, the graph does not contain a cycle "

# ====== Time Complexity Test Section ======
#print static2L()