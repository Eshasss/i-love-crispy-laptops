class Solution:
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[0 if i == j else 10**9 for j in range(n)] for i in range(n)]
        for l in range(2, n + 1): 
            for i in range(n - l + 1):  
                j = i + l - 1  
                for k in range(i, j):  
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + max(arr[i:k+1]) * max(arr[k+1:j+1]))

        return dp[0][n - 1]


        