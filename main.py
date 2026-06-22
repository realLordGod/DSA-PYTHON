# def linear_search(arr,x):
#     for i in range(len(arr)):
#         if x==arr[i]:
#             return i
#     return -1



    

# def binary_search(arr,x):
#     arr.sort()
#     left=0
#     right=len(arr)
#     mid=(left+right)//2
#     while left<=right:
#         if x==arr[mid]:
#             return mid
#         elif x<arr[mid]:
#             mid=mid-1
#         else:
#             mid+=1
    

# def binart_search(arr,x,i,j):
#     mid=i+(j-i)//2
#     while(i<=j):
#         if x==arr[mid]:
#             return mid
#         elif arr[mid]<x:
#             return binart_search(arr,x,mid+1,j)
#         else:
#             return binart_search(arr,x,i,mid-1)
        

# arr=[1,2,3,4,5,6,7,8,9,10]
# x=10
# i=0
# j=len(arr)
# res=binart_search(arr,x,i,j)
# print(res)



# def binary_search(arr,x,i,j):
#     m=i+(j-i)//2
#     while i<=j:
#         if arr[m]==x:
#             if arr[m-1]!=x:
#                 return m
#         else:
#             return binary_search(arr,x,m+1,j)


# # fuction calling 
# arr=[1,2,3,4,5,2,7,43,3,"x","x","x"]
# i=0
# j=len(arr)
# x="x"
# res=binary_search(arr,x,i,j)
# print(res)



# def req_sum(arr,target):
#     left=0
#     right=len(arr)-1
#     while (left<right):
#         sum=arr[left]+arr[right]
#         if sum!=target:
#             if sum<target:
#                 left+=1
#             else:
#                 right-=1
#         else:
#             return left,right, arr[right],arr[left]
    


# arr=[20,40,60,80,90,120,240]
# target=210
# res=req_sum(arr,target)
# print(res)





# price=[7,1,5,3,6,4]
# def findMaxProfit(arr):
#     min_price=float("inf")
#     max_profit=0
#     for i in range(len(arr)):
#         if arr[i]<min_price:
#             min_price=arr[i]
#         elif (arr[i]-min_price>max_profit):
#             max_profit=arr[i]-min_price
#     return max_profit

# x=findMaxProfit(price)
# print(x)




# 2D matrices binary search 
# arr=[[1,2,4,5],[6,7,8,9],[11,12,13,15]]
# target=2
# def binarySearch2D(arr,target):
#     m=len(arr)
#     if m==0:
#         return False
#     n=len(arr[0])
#     left=0
#     right=m*n-1
#     while (left<=right):
#         mid=left+(right-left)//2
#         mid_element=arr[mid//n][mid%n]
#         if target==mid_element:
#             return True
#         elif target<mid_element:
#             right=mid-1
#         else:
#             left =mid+1
#     return False

# x=binarySearch2D(arr,target)
# print(x)


'''
def trinarySearch(arr,i,j,key):
    mid1=i+(j-i)//3
    mid2=j-(j-i)//3

    while (i<=j):
        if arr[mid1]==key:
            return mid1
        elif arr[mid2]==key:
            return mid2
        
        elif key < arr[mid1]:
            return trinarySearch(arr,i,mid1-1,key)
        elif key > arr[mid2]:
            return trinarySearch(arr,mid2+1,j,key)
        else:
            return trinarySearch(arr,mid1+1,mid2-1,key)
        
    return -1 


def binarySearch(arr,key):
    i=0
    j=len(arr)-1
    mid=i+(j-i)//2
    while(i<=j):
        mid=i+(j-i)//2
        if arr[mid]!=key:
            if arr[mid]<key:
                i=mid+1
            elif arr[mid]>key:
                j=mid-1

        else:
            return mid
        
    return -1




arr=[20,25,47,56,59,63,65,79,82]
pos1=binarySearch(arr,82)
print("1",pos1)
pos2=binarySearch(arr,30)
print("2",pos2)
i=0
j=len(arr)-1
pos3=trinarySearch(arr,i,j,47)
print("3",pos3)


'''


# SORTING 

'''
arr=[4,3,2,5,6,7,1,9,8]
n=len(arr)-2
for i in range(0,n):
    if arr[i]>arr[i+1]:
        c=arr[i+1]
        arr[i+1]=arr[i]
        arr[i]=c

        

    for j in range(0,n-1):
        if arr[j]> arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
        

print(arr)


'''



# Insertion sort
'''
def insertionSort(arr):
    for i in range(1,len(arr)-1):
        key = arr[i]
        j=i-1
        while j >=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

print(insertionSort([5,2,9,1,5,6]))

'''

# heapSort

# before going ahead we have to understand binary tree  

'''
1. full binary tree  --> every node should have 0 or 2 children
2. complete binary tree --> all levels should be completely filled except possibly the last level
3. perfect binary tree --> all leaf nodes should be at same level
'''

 
#  minheap --> every parent node should be smaller than its children nodes
# insertion in minheap --> we insert the element at the end and 
# then compare it with its parent node if its smaller we swap 
# them and continue this process until the heap property is satisfied
# delete_minheap --> we remove the root node and replace it with the last element
# 
# 
# 
# creating a minheap
# we can represent a binary tree using an array
# for any node at index i
# left child index = 2*i + 1
# right child index = 2*i + 2
# parent index = (i-1)//2 


# class MinHeap:
#     def __init__(self):
#         self.heap=[]
    
#     def insert(self,key):
#         self.heap.append(key)
#         self._heapify_up(len(self.heap)-1)
    
#     def _heapify_up(self,index):
#         parent_index=(index-1)//2
#         if index>0 and self.heap[index]<self.heap[parent_index]:
#             self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
#             self._heapify_up(parent_index)
    
#     def delete_min(self):
#         if len(self.heap)==0:
#             return None
#         if len(self.heap)==1:
#             return self.heap.pop()
#         root=self.heap[0]
#         self.heap[0]=self.heap.pop()
#         self._heapify_down(0)
#         return root
    
#     def _heapify_down(self,index):
#         smallest=index
#         left_child=2*index+1
#         right_child=2*index+2

#         if left_child<len(self.heap) and self.heap[left_child]<self.heap[smallest]:
#             smallest=left_child
#         if right_child<len(self.heap) and self.heap[right_child]<self.heap[smallest]:
#             smallest=right_child
#         if smallest!=index:
#             self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
#             self._heapify_down(smallest)
    
#     def get_min(self):
#         if len(self.heap)==0:
#             return None
#         return self.heap[0]
    
#     def size(self):
#         return len(self.heap)       
 



# arr=[2,3,5,8,9,10]
# def binary_search(arr,x):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=left+(right-left)//2
#         if arr[mid]!=x:
#             if arr[mid]<x:
#                 left=mid+1
#             else:
#                 right=mid-1
#         else:
#             return mid
#     return left
                
# print(binary_search(arr,7))




# def binary_search(arr,x):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=left+(right-left)//2
#         if arr[mid]!=x:
#             if arr[mid]<x:
#                 left=mid+1
#             else:
#                 right=mid-1
#         else:
#             return mid
#     return -1

# nums=[4,5,6,7,1,2,5]

# print(arr[-1])

# nums = [4,3,2,7,8,2,3,1]

# def findDisappearedNumbers(nums):
#     for num in nums:
#         idx = abs(num) - 1
#         print(idx)
#         if nums[idx] > 0:
#             nums[idx] *= -1

#     res = []
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             res.append(i + 1)
#     return res

# nums=[0,2,1,5,3,4]
# print([nums[i] for i in nums])


# print(findDisappearedNumbers(nums))

# nums=[9,4,20,3,10,5]

# def Subarray(nums,k):
#     count=0
#     has_amp={0:1}
#     pre_sum=0
#     for x in nums:
#         pre_sum+=x
#         if (pre_sum-k) in has_amp:
#             count+=has_amp[pre_sum-k]

#         has_amp[pre_sum]=has_amp.get(pre_sum,0)+1

#     return count
        
# print(Subarray(nums,33))

# nums=[3,1,2,1]

# def Subarry(nums,k):
#     count=0

#     pre_sum=0
#     for i in range(len(nums)):
#         if nums[i]==k:
#             count+=1
#             pre_sum=0
#         pre_sum+=nums[i]
#         r=i+1
#         while r<len(nums) and pre_sum<k:
#             pre_sum+=nums[r]
#             if pre_sum==k:
#                 count+=1
#                 pre_sum=0

#             elif pre_sum<k:
#                 r+=1

#     return count

# print(Subarry(nums,3))


# arr=[1,2,3,4,5,6]

# def CheckSort(arr,i):
#     if i==len(arr)-1:
#         return True
#     elif arr[i]>arr[i+1]:
#         return False
        
#     else:
#         return CheckSort(arr,i+1)
        
# print(CheckSort(arr,0))




# arr=[2,4,6,8,10]
# def twoSum(nums,i,j,k):
#     if i>=j:
#         return [-1,-1]
#         return [i,j] 


#     if nums[i]+nums[j]==k:
#         return [i,j] 
#     elif nums[i]+nums[j]<k:
#         return  twoSum(arr,i+1,j,k)
        
#     else:
#         return twoSum(arr,i,j-1,k)
        
#     # return [-1,-1]
    
    
# print(twoSum(arr,0,len(arr)-1,55))


# s="abcdac"
# t="dacabc"

# def isAnagramRecursive(s,t):
#     if len(s)!=len(t):
#         return False
#     if not s and not t:
#         return True
#     if s[0] in t:
#         return isAnagramRecursive(s[1:],t.replace(s[0],"",1))
#     else:
#         return False

def FirstLast(arr,x):
    l=0
    r=len(arr)-1
    while(l>r):
        if arr[l]==x and arr[r]==x:
            return r-l
        
        elif arr[l]!=x:
            l+=1
        elif arr[r]!=x:
            r-=1

        if arr[l]==x:
            r-=1

        if arr[r]==x:
            l+=1
    return -1

arr=[1,2,3,4,2,2,6,7,2]
print(FirstLast(arr,2))


