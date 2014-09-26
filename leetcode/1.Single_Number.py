# Problems    : Single Number 
# Description : Given an array of integers, every element appears twice except for one. Find that single one.
# Author      : HomeWay88
# Date        : 2014-09-24
# Article-Link: http://www.coderblog.cn/article/46/

import sys

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ret = 0
        for num in A:
            ret ^= num
        return ret

def PasreFromArgs():
	try:
		string = sys.argv[1]
		nums = [int(num) for num in string.split(",")]
		return nums
	except:
		return []

default = [1,2,3,4,3,2,1]
nums = PasreFromArgs()
nums = nums if nums else default

solution = Solution()
result = solution.singleNumber(nums)
print "Numbers:",nums
print "Single Number:",result

