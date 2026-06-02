class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       num= sorted(nums)
       return num

       def merge(arr,L,M,R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            
            i,j,k = L,0,0

            while j<len(left) and k<len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j +=1
                else:
                    arr[i] = right[k]
                    k += 1
                i +=1

            while j < len(left):
                a[i]= left[j]
                j +=1
                i +=1
            while k < len(right):
                a[i]= right[k]
                k +=1
                i +=1

       def mergesort(arr,l,r):
        if l>=r:
            return
        
            m = [l+r] // 2
            mergesort(arr,l,m)
            mergesort(arr,r,m+1)
            merge(arr,l,m,r)
       mergesort(nums,0,len(nums)-1)
       return nums
