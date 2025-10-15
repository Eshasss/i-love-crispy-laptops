class Solution(object):
    def uniquePathsWithObstacles(self, o):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if o[0][0] == 1 or o[-1][-1] == 1:
            return 0 
        m = len(o)
        n = len(o[0])
        dp =  [[0] * n for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if o[i][j] == 0:
                    if i != 0 and j != 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    elif i == 0 and j != 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0 and i != 0 :
                        dp[i][j] = dp[i-1][j]
                    else: # i = j = 0
                        pass 
        #print(dp)
        return dp[m-1][n-1]