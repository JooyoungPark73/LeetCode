import numpy as np
import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = copy.deepcopy(board)
        for x_val in range(len(temp[0])):
            for y_val in range(len(temp)):
                neighbour_live = self.neighbour_checker(temp, x_val, y_val)
                if board[y_val][x_val] == 0 and neighbour_live == 3:
                    board[y_val][x_val] = 1
                elif board[y_val][x_val] == 1 and 2 <= neighbour_live <= 3:
                    board[y_val][x_val] = 1
                elif board[y_val][x_val] == 1:
                    board[y_val][x_val] = 0
        
    def neighbour_checker(self, board, x, y):
        neighbor_live = 0
        for x_val in range(x-1, x+2):
            for y_val in range(y-1, y+2):
                if x_val < 0 or x_val > len(board[0])-1:
                    continue
                elif y_val < 0 or y_val > len(board)-1:
                    continue
                elif x_val == x and y_val == y:
                    continue
                else: neighbor_live += board[y_val][x_val]
        return int(neighbor_live)