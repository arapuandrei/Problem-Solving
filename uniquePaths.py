class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1]*n]*m

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        return grid[-1][-1]