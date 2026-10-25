class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check(nums: List[str]) -> bool:
            maps = set()
            for n in nums:
                if n in maps:
                    return False
                else:
                    maps.add(n)
            return True

        n = len(board)
        for i in range(n):
            nums = []
            for j in range(n):
                if board[i][j] != '.':
                    nums.append(board[i][j])
            if not check(nums):
                return False

        for j in range(n):
            nums = []
            for i in range(n):
                if board[i][j] != '.':
                    nums.append(board[i][j])
            if not check(nums):
                return False

        for r in [[0,1,2], [3,4,5], [6,7,8]]:
            
            for c in [[0,1,2], [3,4,5], [6,7,8]]:
                nums = []
                for i in r:
                    for j in c:
                        if board[i][j] != '.':
                            nums.append(board[i][j])
                            
                if not check(nums):
                    return False
            
        return True



        
