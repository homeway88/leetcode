# Problems	: Candy
# Description : There are N children standing in a line. Each child is assigned a rating value.
#			   You are giving candies to these children subjected to the following requirements:
#				   Each child must have at least one candy.
#				   Children with a higher rating get more candies than their neighbors.
#			   What is the minimum candies you must give?
# Author	  : HomeWay88
# Date		: 2014-09-26
# Article-Link: http://www.coderblog.cn/article/56/

import sys

class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		if ratings == None:
			return 0
		elif len(ratings) <= 1:
			return len(ratings)
		else:
			total = 0
			last = 65535*65535
			candy = 0
			extra = 0
			down_start_index = -1
			last_up_candy = -1
			for i,num in enumerate(ratings):
				if num > last:
					candy += 1
					down_start_index = -1
					last_up_candy = candy

				elif num < last:
					if down_start_index == -1:
						down_start_index = i
					candy = 1
					extra = i - down_start_index

					if down_start_index - 1 > 0:
						if ratings[down_start_index-1] > ratings[down_start_index]:
							if extra+1 >= last_up_candy:
								extra += 1
				else:
					candy = 1
					down_start_index = i

				last = num
				total += candy + extra
				extra = 0

		return total

def PasreFromArgs():
	try:
		string = sys.argv[1]
		nums = [int(num) for num in string.split(",")]
		return nums
	except:
		return []


test_cases = {
	1 : [1],
    2 : [1,1],
    3 : [1,2],
    4 : [1,2,2],
    20 : [1,5,10,4,3,2,1,5],
    9 : [1,4,1,4,1,4],
    9 : [4,1,4,1,4,1],
    5 : [4,4,4,1],
    9: [4,4,4,1,3,3,3],
    11:[4,4,4,1,3,3,3,1],
    9 : [4,2,3,4,1]
	}

#default = [1,5,10,4,3,2,1,5]
default = [4,4,4,4,4,1]
nums = PasreFromArgs()
nums = nums if nums else default

solution = Solution()

for result in test_cases:
	print "Testing:",test_cases[result],
	assert solution.candy(test_cases[result]) == result
	print '=>',result,' ,Passed'

result = solution.candy(nums)
print "Children Ratings:",nums
print "Minimum Candies:",result
