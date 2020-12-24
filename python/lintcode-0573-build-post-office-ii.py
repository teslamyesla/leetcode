"""
Time: O(H * n * m), H is number of houses, m * n is matrix size
Space: O(n * m)

枚举房子的位置。
从每个房子出发，计算房子到所有空地的距离
在每个空地上累加所有房子的距离
最后再找能够到达所有房子且距离之和最小的空地

时间复杂度 O(HOUSE n m)，最坏情况 O(n^2 * m^2)

"""


class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    """
    Reference: https://www.jiuzhang.com/problem/build-post-office-ii/#tag-lang-python
    
    此题难点在于需要逆向考虑 逆向思维从house开始BFS 否则从empty开始会TLE 还是有点费脑子的 这个题告诉我们 当TLE时候 去集合中找找其他部分数量少的 来进行操作 尤其对这种单一操作BFS时间消耗大的题目
    
    对每个house做BFS， 记录每个empty： 
    1. 能被多少个house触及 
    2. 这些能触及的house到达这个empty的总步数之和

    如果最后每个empty都无法被所有house触及 (即不等于house个数)，则返回 -1
    如果有能被所有house触及的empty，取其最小的返回
    """
    def shortestDistance(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        reachable_count = [[0 for _ in range(n)] for _ in range(m)]
        houses = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, m, n, i, j, dist, reachable_count)
                    houses += 1
                    
        min_dist = float('inf')            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reachable_count[i][j] == houses and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
     
        return min_dist if min_dist != float('inf') else -1
        
    def bfs(self, grid, m, n, x, y, dist, reachable_count):
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[x][y] = True
        queue = [(x, y, 0)]
        
        while queue:
            i, j, level = queue.pop(0)
            if dist[i][j] == float('inf'):
                dist[i][j] = level
            else:
                dist[i][j] += level
            
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                
                if ni >= 0 and ni < m and nj >= 0 and nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True 
                    if grid[ni][nj] == 0:  # You cannot pass through wall and house, thus only queue empty
                        queue.append((ni, nj, level + 1))
                        reachable_count[ni][nj] += 1
                        
        return
            
        
                    
                
