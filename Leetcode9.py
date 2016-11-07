#数字一半倒转的方法
class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if 0<= x <10:        #如果数字是0到9的值，直接返回True
			return True
		if x>0 and x%10==0:  #如果x是10的倍数的整数，那直接返回False，因为末尾是0的情况下，不可能是回数
			return False
		remainder=0          #设置余数=0
		while x > remainder:      #这道题目的关键点，将数字分为前后2部分，前半部分是x，后半部分是remainder
									#如果是偶数位数字的话，前半部分和后半部分对半开，并且相等，也能跳出while循环
									#如果是奇数位数字的话，当前半部分小于后半部分的时候，跳出循环
			remainder = remainder + x%10    #每次循环，将前半部分的位数通过取余数提取出来
											#在下一次循环中，通过上一轮的余数×10，再加上本轮的提取出的余数，可以实现倒转
			x=x//10         #提取完余数以后，前半部分向前进一位，方式是通过地板除取整
		print (remainder,x)
		return x==remainder or x==remainder//10  #这是第二个关键点，如果是偶数位数字，那通过反转的后半部分和前半部分应该一样
												#如果是奇数位的数字的话，将后半部分再次地板除10，这样就能剔除最后一位
												#为什么可以提出最后一位呢？因为作为奇数位的数字来说，中间值是不需要比较的
		

#数字整体倒转的方法
class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		original = x   #复制一份原始x
		reverse = 0    #倒转数字初始为0
		if x <0:       #如果x是负数，直接返回False
			return False
		if x!=0 and x%10==0:    #如果x是正数，且能被10整除，返回False
			return False		
		while x>0:              #x>0的意思是，原始值还有位数没有被取干净，还有剩余位数
			reverse = reverse*10 + x%10  #通过取余数来倒转数字
			x=x//10					#每次地板除以后取整
		return reverse == original       #比较倒转后的数字和初始数字
		
s=Solution()
s.isPalindrome(1)
	