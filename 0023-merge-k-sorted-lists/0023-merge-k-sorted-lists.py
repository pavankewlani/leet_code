# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        nodes = []
        for head in lists:
            temp = head
            while temp:
                nodes.append(temp.val)
                temp = temp.next
        
        nodes.sort()
        
        if not nodes:
            return None
        
        head = ListNode(nodes[0])
        temp = head
        for i in range(1, len(nodes)):
            temp.next = ListNode(nodes[i])
            temp = temp.next
            
        return head