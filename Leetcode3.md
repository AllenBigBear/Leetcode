**[原题地址](https://leetcode.com/problems/longest-substring-without-repeating-characters/)**


![](https://github.com/AllenBigBear/Leetcode/blob/master/Images%20for%20Leetcode/Leetcode3.jpg)

>**题目要求如上，寻找字符串中长度最长的没有重复元素的子链
先贴自己的ugly的解答方法，非常土，效率很低，不过能完成所有的答案输出**

```python
class Solution(object):  
    def lengthOfLongestSubstring(self, s):  
        """ 
        :type s: str 
        :rtype: int 
        """  
        longest=0  
          
        result=[]  
        if len(s)==0:  
            return 0  
        elif len(s)==1:  
            return 1  
        elif len(s)==2:  
            if s[0]==s[1]:  
                return 1  
            else:  
                return 2  
        else:  
            for i in range(len(s)-1):  
                temp=s[i]  
                length=0  
                for j in range(i+1,len(s)):  
                    if s[j] not in temp:  
                        temp += s[j]  
                        if j == len(s)-1:  
                            length=len(temp)  
                            result.append(length)  
                    else:  
                        length=len(temp)  
                        result.append(length)  
                        temp=""  
            return max(result)
```

>**再来看别的筒子逼格高的写法，用的是双指针的写法**

```python
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
```

###自己画了下图，初始状态：例子是 s= "abcdba"

![](https://github.com/AllenBigBear/Leetcode/blob/master/Images%20for%20Leetcode/Leetcode3_1.jpg)

当完成当迭代完 index = 0 ,1, 2 , 3的时候，left_edge = 0 , d = { 'a':0 , 'b':1, 'c':2, 'd': 3}
当迭代到index =4的时候，由于index=4的b和index=1的b冲突了，而且，字典里面的b对应的值，也就是1，是大于等于左边界的
所以左边界要变成相同元素左边那个的右边+1位置，以防止同一字串里面出现2个相同元素
>因为在遇到重复元素前，前面的不重复连续的最大长度已经被计算出来了！！！

![](https://github.com/AllenBigBear/Leetcode/blob/master/Images%20for%20Leetcode/Leetcode3_2.jpg)

最后是碰到了a，虽然 a in d ，但是，由于在碰到第二个a之前，字典里的a对应的值是0，向左超出左边界了，所以不生效
可以试想一下，如果不加这句判断重复元素是否在左边界右方的话。
左边界指针又要回到第1号位置了，这显然是错误的！！
所以，这个例子最后的最大长度是4。
