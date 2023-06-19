#https://velog.io/@jinseock95/23.Merge-k-Sorted-Lists

import heapq
import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[List[ListNode]]):
        root = result = ListNode(None)
        heap =[]
        # 각 연결리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
