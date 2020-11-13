"""
Time: O(N*M)
Space: O(N*M)

多源点BFS, Reference: 
https://www.lintcode.com/problem/zombie-in-matrix/solution
https://www.jiuzhang.com/problem/zombie-in-matrix/#tag-lang-python

设地图的大小为N * M。
时间复杂度
    宽度优先搜索遍历整张图的时间复杂度为O(N * M)。
    
空间复杂度
    宽度优先搜索队列的开销为O(N * M)。
    
Notes:
1. no need to keep visited tracker, visited has value 1 and not in the initial queue (not the initial zombies), whenever meet 1 again, it's visited
2. when meeting 1 or 2: continue; when meeting 0: value change to 1 and append to queue
3. return days - 1 instead of days: because days is the # of levels, days - 1 is the propagation between levels

"""

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        queue = []
        
        # get the zombies into queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        
        days = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_i, next_j = i + di, j + dj
                    if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                        continue
                    if grid[next_i][next_j] == 1 or grid[next_i][next_j] == 2:
                        continue
                    grid[next_i][next_j] = 1
                    queue.append((next_i, next_j))
            days += 1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return -1
            
        return days - 1 
                        
