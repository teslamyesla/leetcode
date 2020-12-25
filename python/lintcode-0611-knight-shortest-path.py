"""
Time: O(n*m)
Space: O(n*m)

时间复杂度O(n*m)
    最多跑一边图 n为图的行数，m为图的列数，最多跑一边图，即n*m
空间复杂度O(n*m)
    所有点的信息 n为图的行数，m为图的列数

Note: mark visited (grid[nx][ny] = 1) before pushing to queue! Instead of after poping from queue 
(because for the ones already in queue but haven't been poped yet, we don't want to push the nodes to queue again)! 

"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1
            
        m, n = len(grid), len(grid[0])
        queue = [(source.x, source.y, 0)]
        grid[source.x][source.y] = 1
         
        while queue:
            x, y, length = queue.pop(0)
            if x == destination.x and y == destination.y:
                return length
            for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    queue.append((nx, ny, length + 1))
                    
        return -1
