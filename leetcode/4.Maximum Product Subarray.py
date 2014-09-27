# Problems    : Maximum Product Subarray
# Description : Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# Author      : HomeWay88
# Date        : 2014-09-27
# Article-Link: http://www.coderblog.cn/article/61/

import sys

class Solution:
    def product(self,A,left,right):
        if left >= len(A):
            return None
        else:
            prd = A[left]
            for n in A[left+1:right]:
                prd *= n
            return prd
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if(len(A)==1):
            return A[0]

        current_product = None
        max_product = max(A)
        cnt = 0
        first = -1
        last = -1
        n = len(A)-1
        start = 0
        for i,num in enumerate(A):
            if num < 0:
                cnt += 1
                if first == -1:
                    first = i
                last = i
            if num == 0 or i==n:
                end = n+1 if num and i==n else i
                if cnt % 2 ==0:
                    current_product = self.product(A,start,end)
                    max_product = max(current_product,max_product)
                else:

                    max_product =  max(max_product,self.product(A,start,last),self.product(A,first+1,end))

                first,last = -1,-1
                start = i+1
                cnt = 0

        return max_product

def PasreFromArgs():
    try:
        string = sys.argv[1]
        nums = [int(num) for num in string.split(",")]
        return nums
    except:
        return []

default = [-1,-2,-3,0,1,2]
nums = PasreFromArgs()
nums = nums if nums else default

solution = Solution()
result = solution.maxProduct(nums)
print "Numbers:",nums
print "Max Product:",result

