class Solution:
    def trap(self, height: List[int]) -> int:

        left = []
        max_left = 0
        right = [0]*len(height)
        max_right = 0
        c = 0
        for i in range(len(height)):
            if height[i]>max_left:
                max_left = height[i]
            left.append(max_left)


        for j in range(len(height)-1, -1, -1):
            if height[j]>max_right:
                max_right = height[j]
            right[j] = max_right

        for k in range(len(height)):
            c += min(left[k],right[k]) - height[k]

        return c

        