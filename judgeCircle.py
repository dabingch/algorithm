class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves: return true
        
        x = y = 0

        for move in moves:
            if move == 'U': y +=1
            elif move == 'D': y -= 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        if x == 0 and y == 0:
            return True
        else:
            return False