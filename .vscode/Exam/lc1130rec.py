class Solution:
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        pos = []
        n = len(arr)
        if n == 2:
            return arr[0] * arr[1]
        for k in range(1, n): 
            ans = max(arr[:k]) * max(arr[k:])
            if len(arr[k:]) > 1:
                ans += self.mctFromLeafValues(arr[k:])
            if len(arr[:k]) > 1:
                ans += self.mctFromLeafValues(arr[:k])
            pos.append(ans)
        return min(pos)

        