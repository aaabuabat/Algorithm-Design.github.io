''' 
This a program with a divide-and-conquer algorithm that finds the two indices (i and j, 1 <= i <=
j <= n) in an array of integers with maximum sum of contiguous elements. For example, if the
array elements are: 2, 18, -22, 20, 8, -6, 10 -24, 13, 3, then the returned indices should be i=4 and
j=7.
'''


# This function will checks elements between the two lists (the left side and the right side), crossing the midpoint.

def MaxCrossingSum(A, first, mid, last):

#======== RIGHT SIDE ======================================
    LargNegativeNumber = -99999 # initial value in case if the array contains any large negative number. 
    summ = 0
    for j in range(mid+1, last+1): #here the loop will start from the middle till the A[n]
        summ = summ + A[j]
        if summ > LargNegativeNumber:
            LargNegativeNumber = summ
            MaxR  = j # in order to tracking the index.
    Rsum  = LargNegativeNumber


#========= LEFT SIDE ======================================
    LargNegativeNumber = -99999 # initial value in case if the array contains any large negative number. 
    summ = 0
    for i in range(mid, first - 1, -1): #here the loop will start from the middle till the A[0]
        summ = summ + A[i] 
        if summ > LargNegativeNumber: 
            LargNegativeNumber = summ
            MaxL  = i # in order to tracking the index.
    Lsum = LargNegativeNumber

#======== RETURN THE VALUES ==============================

    return(MaxL, MaxR, Lsum + Rsum) 

def GetMax(a,x,y): # To get the max sum between the three sections. 
    if a >= x and a >= y:
        return True 
    else:
        return False 

# This function will checks each side separately and call itself and the first function (recursively) till fineshed all the elements in the array, this actually the leading function here. 
def MaximumSumSubarray(A, first, last):

    if last == first:
     return first, last, A[first] #that means the array has one elemnt.

    else:
        mid = (first+last)/2

    Lfirst, LLast, LSum  = MaximumSumSubarray (A,first,mid)  #continuing to check the left side (recursively). 
    Rfirst, RLast, RSum  = MaximumSumSubarray (A,mid+1,last) #continuing to check the right side (recursively).
    Cfirst, CLast, CSum  = MaxCrossingSum (A,first,mid,last) #continuing to check the middle (recursively).

        # this part will make a comparison between the three sides (left , right , and if the largest value well occurs between the two sides)       
       

    if   GetMax (LSum,RSum,CSum):
           return Lfirst, LLast, LSum
    elif GetMax(RSum,LSum,CSum):
           return Rfirst, RLast, RSum
    else:
           return Cfirst, CLast, CSum

# ================ Test Section =============
# Test case-1 : 
# A = [2, 18, -22, 20, 8, -6, 10,-24,13,3]  
# Test case-2 :                                   
# A = [-9,-5,-2,-1]   
# Test case-3 :                                                                                             
A = [2,8,-9,20,25,-127,90,50,-89,-2,125,64,8,-15,-8,10,11,-30,22] 

# first,last,MaximumSum = MaximumSumSubarray(A, 0, 9)
# first,last,MaximumSum = MaximumSumSubarray(A, 0, 3)
first,last,MaximumSum = MaximumSumSubarray(A, 0, 18)

print(first)
print(last)
print(MaximumSum)