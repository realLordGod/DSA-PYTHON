
# #Binary Search


# def binary_search(arr,k):
#     l=0
#     r=len(arr)

#     while(r>=l):
#         m=l+(r-l)//2

#         if arr[m]==k:
#             return m

#         elif arr[m]>k:
#             r=m-1

#         else:
#             l=m+1
#         return -1


# arr=[1,2,4,5,6,7,10]
# k=7

# # print(binary_search(arr,k))


# #SORTING ALGORITHMS

# #Bubble Sorting


# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#              arr[j],arr[j+1]=arr[j+1],arr[j]

#     return arr




# #print(bubble_sort(arr))


# #Selection Sorting

# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         min=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min]:
#                 min=j


#         arr[i],arr[min]=arr[min],arr[i]

#     return arr

# #print(selection_sort(arr))



# """Insertion Sort """


# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         j=i-1
#         key=arr[i]
#         while (j>=0 and key<arr[j]):
#             arr[j+1]=arr[j]
#             j-=1

#         arr[j+1]=key

#     return arr
# #arr=[75,90,100,95,85,80]
# #print(insertion_sort(arr))

# ''' Dividing and Conquer '''

# def findMaxMin(arr,i,j):
#     if i==j:
#         max_val=arr[i]
#         min_val=arr[i]

#     elif i==j-1:
#         if arr[i]>arr[j]:
#             max_val=arr[i]
#             min_val=arr[j]
#         else:
#             max_val=arr[j]
#             min_val=arr[i]

#     else:
#         m=i+(j-i)//2
#         max1,min1=findMaxMin(arr,i,m)
#         max2,min2=findMaxMin(arr,m+1,j)


#         if max1<max2:
#             max_val=max2
#         else:
#             max_val=max1

#         if min1<min2:
#             min_val=min1
#         else:
#             min_val=min2
#     return max_val,min_val



# #arr=[1,2,4,2,5,33,5]
# #i=0
# #j=len(arr)-1
# #print(findMaxMin(arr,i,j))



# def Power(a,n):
#     if n==1:
#         return a
#     elif n==0:
#         return 1

#     else:
#         m=n//2

#         b=Power(a,m)
#         result=b*b

#         if n>0:
            
#             if n%2==0:
#                  return result
#             else:
#                  return result*a

#         else:
#             if n%2==0:
#                  return 1/result
#             else:
#                  return 1/result*a




# print(Power(2,16))



# def CountStep(n):
#     if n==2:
#         return 2
#     elif n==1:
#         return 1
#     else:
#         return CountStep(n-1)+CountStep(n-2)

# """Approach 1"""


# def collinear(x1,x2,x3,y1,y2,y3):
#     area=0.5*(x1*(y2-y3)+x2*(y3-y2)+x3*(y1-y2))
#     if 0==area:
#         return "Points are Collinear"
#     else:
#         return "Points are Non Collinear"


# """Aproach 2"""

# def CheckCollinear(x1,x2,x3,y1,y2,y3):
#     if ((y2-y1)*(x3-x2)==(x2-x1)*(y3-y2)):
#         return "Collinear"
#     else:
#         return "Non Collinear"


# print(CheckCollinear(1,1,1,6,0,9))




# def findme153(nums,x):
#     l=0
#     r=len(nums)-1

#     while(r>l): # even r=0 and l=0 this condition will break

#         m=l+(r-l)//2

#         if nums[m]>nums[r]: # if left side of the array is bigger then right side of the array then we have to move our pointer to the right side
#             l=m+1

#         else:  # if right is grater then we are moving to the left side
#             r=m


#     return nums[l]





def maxpro152(nums):

    pre_max=nums[0]
    pre_min=nums[0]
    max_p=nums[0]

    for x in nums[1:]:
        
        if x<0: # if x<0 means our pre_min which is negative with multiply of another negative no, it will give me positive
            pre_max,pre_min=pre_min,pre_max

        
        pre_max=max(x,pre_max*x)
        pre_min=min(x,pre_min*x)


        max_p=max(pre_max,max_p)


    return max_p






    


    
    








