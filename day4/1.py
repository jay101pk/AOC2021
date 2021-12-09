import re

def CheckBoard(board : list[bool]) -> bool:
    for i in range(5):
        if all([board[x + i * 5] for x in range(5)]):
            return True
        if all([board[x * 5 + i] for x in range(5)]):
            return True

    return False

file = open("input", "r")
lines = file.readlines()

draws = [int(x) for x in re.findall(r'\d+', lines[0])]

boards = [[int]]
for i in range(100):
    board = []
    for j in range(5):
        for x in re.findall(r'\d+', lines[i * 6 + j + 2]):
            board.append(int(x))
    boards.append(board)

marked = [[False for _ in range(25)] for _ in range(100)]
win = -1
winBoard = -1
for draw in draws:
    for (index,board) in enumerate(boards):
        try:
            i = board.index(draw)
            marked[index][i] = True
        except:
            pass
    
    b = False
    for (index,board) in enumerate(marked):
        if CheckBoard(board):
           win = draw
           winBoard = index 

    if win > -1:
        break



unmarked = [boards[winBoard][x] for x in [i for i in range(25) if not marked[winBoard][i]]]
print(win * sum(unmarked))