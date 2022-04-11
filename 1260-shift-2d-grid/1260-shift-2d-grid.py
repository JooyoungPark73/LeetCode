import numpy as np

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid_np = np.array(grid)
        a = grid_np.flatten().tolist()

        k = k%len(a)
        popped = []
        for i in range(k):
            popped.append(a.pop())
        popped.reverse()
        a = popped + a
        
        a = np.array(a)
        a = a.reshape(np.shape(grid_np)).tolist()
        return a