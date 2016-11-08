#coding=utf-8
class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		length = len(s)  #总共有多少元素
		step = 2*numRows-2      #有几列, 2n-2 = 0+(n-1)+(n-2)+1
		
		if s == "":      #如果空字符串，返回空字符串""
			return ""
		if length<numRows or numRows ==1 :       #如果只有一行，则直接返回原字符串
			return s
		result = s[::step] #这是第一行，他通过切片的步进step来取值，因为每个元素都是间隔一个step
						  #这题里面，首行和尾行是特殊的，所以要区别对待
		for i in range(1,numRows-1):  #开始迭代除了第一行和最后一行之外的中间所有行
			for j in range(i,length,step): #这里关键的地方，他将图形在纵向上进行切割，以每个step为标准开头，进行迭代
				result += s[j]        #在每次切割后，进行添加的第一个元素，应该是每一行的开头的元素加上某倍数的step
				if j+(step-i*2) < length:  #如果斜线上的元素是在总长度以内的
					result += s[j+step-i*2] #那么，就添加此元素
		result += s[numRows-1::step] #最后一行开始迭代		
		print (result)
		return result

s=Solution()
s.convert('abcdefghi',4)
s.convert('',4)
s.convert('abc',6)