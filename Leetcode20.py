class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 !=0:         #如果元素个数是单数，直接枪毙
            return False
        if not s:                #如果是空字符串，返回True
            return True
        a={')':'(', '}':'{', ']':'['}   #这题的关键，将结尾括号和开始括号一一对应起来，并且用结尾符号作为键
        stack = []                      #初始化一个列表，作为stack的结构
        for i in s :                    #历遍s的每个元素
            if i in '({[':              #如果元素是开始括号的一种
                stack.append(i)         #把元素添加进stack
            elif i in ')}]':            #如果是结尾符号
                if not stack:           #如果此时stack是空的，直接返回False，比如"[])"这种情况
                    return False
                elif stack and stack.pop() != a[i]: #如果stack非空，但是最后一个元素和当前元素再字典a里面取出的值不一样
                    return False                    #也返回False
            else:
                return False            #如果i不在以上范围内，直接返回False
        if stack:                       #如果结束历遍以后，stack还是非空，返回False
            return False
        else:                           #如果历遍结束以后，stack为空，则返回True
            return True