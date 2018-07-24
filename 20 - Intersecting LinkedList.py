# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        aLength = 0
        currentA = headA
        while currentA != None:
            aLength += 1
            currentA = currentA.next

        bLength = 0
        currentB = headB
        while currentB != None:
            bLength += 1
            currentB = currentB.next

        difference = abs(bLength-aLength)
        if aLength > bLength:
            currentA = headA
            while difference > 0:
                currentA = currentA.next
                difference -= 1

            currentB = headB
            while currentA != None:
                if currentA.val == currentB.val:
                    return currentA
                currentA = currentA.next
                currentB = currentB.next
            return None

        else:
            currentB = headB
            while difference > 0:
                currentB = currentB.next
                difference -= 1

            currentA = headA
            while currentB != None:
                if currentA.val == currentB.val:
                    return currentB
                currentA = currentA.next
                currentB = currentB.next
            return None
