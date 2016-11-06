class Solution(object):  
    def lengthOfLongestSubstring(self, s):  
        """ 
        :type s: str 
        :rtype: int 
        """  
        left_edge = 0   #设立左边界值，也就是指针1  
        longest = 0     #设定变量以保存出现过的最大值  
        d = {}          #很关键的一个hash表，也就是字典，用来储存一个元素最近出现的位置  
        for index,value in enumerate(s):              #将字符串的下标和值对应取出  
            if value in d and d[value] >= left_edge:  #如果这个值，出现在字典的key中，并且，这个值对应的下标大于等于左边界  
                left_edge = d[value]+1            #则左边界就变成左边那个重复值的右边一位  
                        #这里要多说几句，这句话的作用是：如果发现有相同元素，则左边界向右移动一位  
                        #因为按照要求，你的答案里面是不能出现同样字符串的  
            d[value]=index      #如果value没有出现过，则添加；如果出现过，则刷新value对应的index值  
                                    #这句又是非常关键的一句，他刷新了重复值出现的最新位置  
                        #也就是，配合第11行的语句，告诉代码，如果这个重复值是出现在左边界的左边  
                        #则这个重复值算法无效，不会把左边界右移  
            longest = max(longest, index-left_edge+1) #每次迭代的过程会把最长值和上一次迭代的比较，刷新最大值  
        return longest