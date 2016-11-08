#coding=utf-8
class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		length = len(s)  #�ܹ��ж���Ԫ��
		step = 2*numRows-2      #�м���, 2n-2 = 0+(n-1)+(n-2)+1
		
		if s == "":      #������ַ��������ؿ��ַ���""
			return ""
		if length<numRows or numRows ==1 :       #���ֻ��һ�У���ֱ�ӷ���ԭ�ַ���
			return s
		result = s[::step] #���ǵ�һ�У���ͨ����Ƭ�Ĳ���step��ȡֵ����Ϊÿ��Ԫ�ض��Ǽ��һ��step
						  #�������棬���к�β��������ģ�����Ҫ����Դ�
		for i in range(1,numRows-1):  #��ʼ�������˵�һ�к����һ��֮����м�������
			for j in range(i,length,step): #����ؼ��ĵط�������ͼ���������Ͻ����и��ÿ��stepΪ��׼��ͷ�����е���
				result += s[j]        #��ÿ���и�󣬽�����ӵĵ�һ��Ԫ�أ�Ӧ����ÿһ�еĿ�ͷ��Ԫ�ؼ���ĳ������step
				if j+(step-i*2) < length:  #���б���ϵ�Ԫ�������ܳ������ڵ�
					result += s[j+step-i*2] #��ô������Ӵ�Ԫ��
		result += s[numRows-1::step] #���һ�п�ʼ����		
		print (result)
		return result

s=Solution()
s.convert('abcdefghi',4)
s.convert('',4)
s.convert('abc',6)