board = [['.', '#', '*', '.', '.'],
         ['.', '.', '.', '.', '.'],
         ['#', '.', '#', '#', '.'],
         ['#', '.', '.', '.', '#']]

import re

def solution(board):
    # Pushing
    p_board = []
    for row in board:
        rowstr = "".join(row)
        # print(">", rowstr)
        while re.search("[#][.]", rowstr):
            rowstr = re.sub("[#][.]", ".#", rowstr)
            # print(">", rowstr)
        p_board.append([obj for obj in rowstr])
    print("B: ",p_board)
    # Falling
    f_board = []
    print(f_board)
    for i in range(0, len(p_board)+1):
        col = [obj[i] for obj in p_board]
        colstr = "".join(col)
        # print(">", colstr)
        while re.search("[#][.]", colstr):
            colstr = re.sub("[#][.]", ".#", colstr)
        # print(">", colstr)
        f_board.append([obj for obj in colstr])
    print(f_board)
    # final board
    fn_board = []
    for i in range(0, len(f_board)-1):
        row = [obj[i] for obj in f_board]
        print(">", "".join(row))
        fn_board.append(row) 
    print(fn_board)

if __name__ == "__main__":
    solution(board)