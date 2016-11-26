# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:             #判断l1或者l2为空的情况
			if not l2:
				return None
			else:
				return l2
        else:
			new = ListNode(0)  #设置一个头结点，用来操作串联所有结点
			flag =new          #赋值一个头结点保留在原地，用来最后返回使用
			while l1 and l2:   #当l1和l2都有值的时候，重复比较
				if l1.val <= l2.val:   #如果l1的值比l2小
					new.next = l1      #那就将头结点指向当前l1
					l1 = l1.next       #并把l1向后移动一位用以刷新l1
				else:
					new.next = l2      #反之，则操作l2
					l2 = l2.next
				new = new.next         #每次比较后，都需要刷新一下new的值
			if l1:                     #如果只剩下l1有值了
				while l1 :          
					new.next = l1      #那就重复串联l1的值一直到结束
					l1 = l1.next
					new = new.next
			if l2:                     #反之操作l2
				while l2 :
					new.next = l2
					l2 = l2.next
					new = new.next
			return flag.next           #最后从头结点指向的结点，也就是第一个比较厚的元素开始返回
