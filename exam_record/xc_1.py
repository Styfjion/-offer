
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def isLoop(self,pHead):
        pFast = pHead
        pSlow = pHead
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                return 'true'
        if not pFast or not pFast.next:
            return 'false'
if __name__ == "__main__":
    line = input().strip()
    nodes = list(map(str, line.split(',')))
    head = ListNode(nodes[0])
    ListNodes = []
    node = head
    for i in range(1,len(nodes)):
        vals = [unit.val for unit in ListNodes]
        if nodes[i] in vals:
            node.next = ListNodes[vals.index(nodes[i])]
            break
        else:
            node.next = ListNode(nodes[i])
            ListNodes.append(node)
        node = node.next
    print(Solution().isLoop(head))
