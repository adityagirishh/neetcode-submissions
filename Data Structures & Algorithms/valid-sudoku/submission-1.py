class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        box = [set() for _ in range(len(board))]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num==".":
                    continue
                if num in rows[i]:
                    return False
                rows[i].add(num)
                if num in cols[j]:
                    return False
                cols[j].add(num)
                box_index = (i // 3) * 3 + (j // 3)
                if num in box[box_index]:
                    return False
                box[box_index].add(num)
        
        return True
                




        