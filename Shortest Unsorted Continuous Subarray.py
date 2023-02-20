class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        rnge = [0] * n
        for x in range(n):
            if not stack:
                stack.append(x)
                rnge[x] = 1
            else:
                while stack and nums[stack[-1]] >= nums[x]:
                    y = stack.pop()
                    rnge[y] = 0
                stack.append(x)
                rnge[x] = 1
        left, right = float('inf'), - float('inf')
        for x in range(n):
            if not rnge[x]:
                left = min(left, x)
                right = max(right, x)
        #print(rnge, left, right)
        if left != float('inf') and right != float('-inf'):
            return right - left + 2
        else: 
            return 0
