# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

    def addTwoNumber2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)  # 头结点，无存储，指向链表第一个结点
        node = head  # 初始化链表结点
        carry = 0  # 初始化 进一 的数
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry  # 对每一位求和
            carry = sum // 10  # 地板除，求进一（其为0或1）
            node.next = ListNode(sum % 10)  # 取余数，求本位结点
            if l1:  # 求空否，防止出现无后继结点
                l1 = l1.next
            if l2:  # 同上
                l2 = l2.next
            node = node.next  # 更新指针
        if carry != 0:  # 验证最后一位相加是否需 进一
            node.next = ListNode(1)
        return head.next


l1 = ListNode([2, 4, 3])
l2 = ListNode([5, 6, 4])
s = Solution()
print(s.addTwoNumber2(l1, l2))
