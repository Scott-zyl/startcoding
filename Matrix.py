# Time: O(m * n)
# Space: O(m * n)

import collections

matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
class Solution():
    def updateMatrix(self, matrix):
        """
        :param matrix: List[list[int]]
        :return:List[list[int]]
        """

        queue = collections.deque()  # deque: list-like container with fast appends and pops on either end
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j))  # record 0
                else:
                    matrix[i][j] = float('inf')

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            cell = queue.popleft()  # deal from 0
            for dir in dirs:
                i, j = cell[0] + dir[0], cell[1] + dir[1]
                if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])) \
                        or matrix[i][j] <= matrix[cell[0]][cell[1]] + 1:
                    continue
                queue.append(i, j)  # second deal
                matrix[i][j] = matrix[cell[0]][cell[1]] + 1
        return matrix

