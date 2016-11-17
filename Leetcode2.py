# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:          #如果l1是空的
            return l2       #直接返回l2
        if not l2:          #如果l2是空的
            return l1       #直接返回l1
        else:
            new = ListNode(0)    #如果两者都是非空的，则建立一个头结点，数据域val=0,指针域暂时为None
            result = new         #复制一份头结点保留在原地开头
            carry = 0            #carry的意思是如果2者相加超过10，则进位以后剩余的值是多少
            while l1 and l2:     #开始循环，当l1和l2都有剩余结点的时候
                add = 0          #两个元素相加的值初始为0
                add = l1.val + l2.val + carry   #两个元素相加的值等于两个元素的值加上进位上来的值
                carry = 0        #值在上一轮进位被使用之后，被清0
                if add > 9:      #如果这一轮的两个元素值相加大于9需要进位
                    carry = add//10  #carry等于进位值，其实也就是1
                    add -= 10        #相加的元素在进位之后减去10
                new.next = ListNode(add)  #将上一个结点和新生成的结点连接起来
                new = new.next       #并将需要计算的结点位置向前挪动一位，作用和指针一样
                l1=l1.next           #将l1和l2的结点各自移动一位
                l2=l2.next
            if l1:               #如果l1比l2长
                while l1:        #循环l1到没有结点
                    add = 0      
                    add = l1.val + carry + 0  #虚拟一个l2的结点元素值为0
                    carry = 0
                    if add > 9:
                        carry = add//10
                        add -= 10
                    new.next = ListNode(add)
                    new = new.next
                    l1 = l1.next
            if l2:               #如果l2比l1长
                while l2:
                    add = 0
                    add = l2.val + carry + 0
                    carry = 0
                    if add > 9:
                        carry = add//10
                        add2 -= 10
                    new.next = ListNode(add)
                    new = new.next
                    l2 = l2.next
            if carry:            #如果总的结束之后，还有进位上来的数，则需要新建一个结点进行连接
                new.next = ListNode(carry)
            return result.next   #result还是停留在头结点的位置，返回的是他的next，也就是第一个结点