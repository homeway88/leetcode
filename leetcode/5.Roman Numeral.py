# Problems    : Roman Numeral
# Description : 1.Given a roman numeral, convert it to an integer.
#               2.Given an integer, convert it to a roman numeral.
# Author      : HomeWay88
# Date        : 2014-10-07
# Article-Link: http://www.coderblog.cn/article/76/

import sys

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s = s.upper() + "I"
        total = 0
        for (v1,v2) in zip(s,s[1:]):
            num1 = roman[v1]
            num2 = roman[v2]
            if num1 < num2:
                total -= num1
            else:
                total += num1
        return total
    # @return a string
    def intToRoman(self, num):
        one= ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        ten = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundred = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousand = ["","M","MM","MMM"]
        result = ''
        result += thousand[num/1000]
        num %= 1000
        result += hundred[num/100]
        num %= 100
        result += ten[num/10]
        num %= 10
        result += one[num]
        return result

def PasreFromArgs():
    try:
        roman = sys.argv[1]
        valid = 'IVXLCDM'
        for c in roman:
            if c not in valid:
                print roman,'is not a valid roman numeral, user IV instead'
                roman = 'IV'
                break
        return roman        
    except:
        return 'IV'

roman = PasreFromArgs()

solution = Solution()
number = solution.romanToInt(roman)
print "Roman -> Integer:",roman,'->',number
print "Integer -> Roman:",number,'->',solution.intToRoman(number)
