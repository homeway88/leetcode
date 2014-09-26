# Problems    : Single Number II
# Description : Given an array of integers, every element appears three times except for one. Find that single one.
# Author      : HomeWay88
# Date        : 2014-09-25
# Article-Link: http://www.coderblog.cn/article/51/

import sys

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in range(32):
            sum = 0
            mask = 1 << i
            for num in A:
                if num & mask:
                    sum += 1
        
            if sum % 3:
                result |= mask
        
        if result & 0x80000000:
            result = -((result ^ 0xFFFFFFFF) + 1)
        return result

def PasreFromArgs():
    try:
        string = sys.argv[1]
        nums = [int(num) for num in string.split(",")]
        return nums
    except:
        return []

default = [1,2,3,4,3,2,1,1,2,3]
nums = PasreFromArgs()
nums = nums if nums else default

solution = Solution()
result = solution.singleNumber(nums)
print "Numbers:",nums
print "Single Number:",result

