# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def joinnumber(head):
            out=""
            while head:
                out+=str(head.val)
                head=head.next
            return int(out[::-1])

        def createlist(num):
            hash_map={}
            for i,val in enumerate(num):
                hash_map[i]=ListNode(int(val),None)
            
            out_len=len(hash_map)

            for i in range(out_len):
                if (i+1)==out_len:
                    hash_map[i].next=None
                else:
                    hash_map[i].next=hash_map[i+1]
            print(hash_map[0].val)
            return hash_map[0]

        numl1=joinnumber(l1)
        numl2=joinnumber(l2)
        # print(numl1)
        # print(numl2)
        return createlist(str(numl1+numl2)[::-1])

            
