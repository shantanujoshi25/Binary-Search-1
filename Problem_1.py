# // Time Complexity : O(log nm) nxm is shape of matrix
# // Space Complexity : O(1)
    
class Solution:


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0]) 
        low=0
        high=m*n-1
        while(low<=high):
            mid = low + (high-low)//2 
            i = mid//m
            j = mid%m

            if(matrix[i][j] == target):
                return True
            elif(matrix[i][j] > target):
                high = mid-1
            else:
                low = mid+1
        return False  