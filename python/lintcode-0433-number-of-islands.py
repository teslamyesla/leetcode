"""
Solution 1: DFS 
Time: O(N * M), where N is # of rows and M is # of columns
Space: worst case O(N * M), in case that the grid map is filled with lands where DFS goes by N * M deep

Solution 2: BFS
Time: O(N * M), where N is # of rows and M is # of columns
Space: O(min(N, M)), in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N)

Complexity Reference: https://www.jiuzhang.com/problem/number-of-islands/#tag-lang-python
https://www.codertrain.co/number-of-islands
https://stackoverflow.com/questions/50901203/dfs-and-bfs-time-and-space-complexities-of-number-of-islands-on-leetcode
"""

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """    
    """
    Solution 2: BFS
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, m, n, i, j)
                    count += 1
                    
        return count
        
    def bfs(self, grid, m, n, i, j):
        queue = [(i, j)]
        grid[i][j] = 0 # visited, mark as 0
        
        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))
                    
        return
        
    """
    Solution 1: DFS
    
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    count += 1
                    
        return count
        
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0: # 0 is sea or visited island
            return
        
        grid[i][j] = 0 # visited, mark as 0
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
        
        return
    """    
                    
