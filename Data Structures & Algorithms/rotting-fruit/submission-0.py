from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxTime = 0
        q = deque()
        fresh = 0

        # same outer scan
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        def bfs(grid, fresh):
            time = 0

            while q and fresh > 0:
                for _ in range(len(q)):
                    i, j = q.popleft()

                    for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        if (ni < 0 or ni >= len(grid) or
                            nj < 0 or nj >= len(grid[ni]) or
                            grid[ni][nj] != 1):
                            continue

                        grid[ni][nj] = 2
                        q.append((ni, nj))
                        fresh -= 1

                time += 1

            return time, fresh

        maxTime, fresh = bfs(grid, fresh)

        return maxTime if fresh == 0 else -1