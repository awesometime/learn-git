# https://leetcode.com/problems/climbing-stairs/discuss/25313/Python-different-solutions-(bottom-up-top-down).

class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        tempArray = [1,2]
        if number >= 3:
            for i in range(3,number+1):
                tempArray[(i+1)%2] = tempArray[0] + tempArray[1]
        return tempArray[(number+1)%2]



    def rectCover1(self,numbers):
        if number<2:
            return number
        a,b=1,1
        for i in range(1,number):
            a,b = b,a+b
		return b
