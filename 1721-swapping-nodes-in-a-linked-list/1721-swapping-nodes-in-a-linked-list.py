# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodelist = []
        node = head
        nodelength = 1
        while node.next != None:
            nodelength += 1
            nodelist.append(node.val)
            node = node.next
        nodelist.append(node.val)
        
        tmp = nodelist[k-1]
        nodelist[k-1] = nodelist[-k]
        nodelist[-k] = tmp
        
        node = head
        for i in range (nodelength):
            node.val = nodelist[i]
            
            node = node.next
        
        return head