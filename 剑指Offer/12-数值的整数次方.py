# 非递归   exponent & 1 == 1 判断exponent为奇偶	
# 不能出现 base==0？？ 的判断	 计算机内表示小数有误差，只能判断他们的差的绝对值是不是在一个很小的范围内
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 0
        #if base==0:
            #return False
        if exponent==0:
            return 1
		if exponent==1:
            return base
        if exponent<0:
            flag = 1
        result=1
        for i in range(abs(exponent)):
            result*=base
        if flag==1:
            result = 1/result
        return result

# 递归
class Solution1:
    def Power(self, base, exponent):
        # write code here
        try:
            ret = self.power_value(base, abs(exponent))
            if exponent < 0:
                return 1.0 / ret
                            
        except ZeroDivisionError:
            print('Error: base is zero')
        else:
            return ret
            
    def power_value(self,base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        ret = self.power_value(base, exponent >> 1) # exp>>1就是exp//2，但是右移效率更高
        ret *= ret
        if exponent & 1 == 1:                       # exp&1就是判断奇偶，=1为奇数，比%效率更高
            ret *= base
        return ret
