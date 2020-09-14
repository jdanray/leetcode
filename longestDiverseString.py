# https://leetcode.com/problems/longest-happy-string/

class Solution(object):
    def longestDiverseString(self, a, b, c):
            heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
            heapq.heapify(heap)
            result = []
            while heap:
                remaining, char = heapq.heappop(heap)
                if remaining == 0:
                    break
                    
                if len(result) >= 2 and result[-1] == char and result[-2] == char:
                    remaining2, char2 = heapq.heappop(heap)
                    if remaining2 == 0:
                        break
                    else:
                        result.append(char2)
                        heapq.heappush(heap, (remaining2 + 1, char2))
                        heapq.heappush(heap, (remaining, char))
                else:
                    result.append(char)
                    heapq.heappush(heap, (remaining + 1, char))
                    
            return "".join(result)
