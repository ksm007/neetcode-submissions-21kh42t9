class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l,r,m):
            lArr = arr[l:m+1]
            rArr = arr[m+1:r+1]
            i,j,k = l,0,0
            while j < len(lArr) and k < len(rArr):
                if lArr[j] <= rArr[k]:
                    arr[i] = lArr[j]
                    j+=1
                else:
                    arr[i] = rArr[k]
                    k+=1
                i+=1
            while j < len(lArr):
                arr[i] = lArr[j]
                j+=1
                i+=1
            while k < len(rArr):
                arr[i] = rArr[k]
                k+=1
                i+=1

        def divide(arr, l,r):
            if l>=r:
                return
            m = (l+r) //2
            divide(arr,l,m)
            divide(arr,m+1,r)
            merge(arr,l,r,m)
        divide(nums, 0, len(nums) - 1)
        return nums