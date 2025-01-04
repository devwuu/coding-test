def other_solution_1(board):

    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    length = len(board)
    cnt = 0

    for i in range(length): # o(n^3) 30 * 30 * 8 = 최대 7200
        for j in range(length):
          if board[i][j] == 1:
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                    cnt += 1
                    board[nx][ny] = 2 # 이미 갯수에 포함되어 있기 때문에 위험 구역에서 제외 처리 함

    return cnt

def my_solution_1(board):

    danger = set()
    dx = [-1, 0, 1, 0, -1, -1, 1, 1] # 상하좌우대각선
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    length = len(board)

    for i in range(length): # o(n^3) 30 * 30 * 8 = 최대 7200
        for j in range(length):
          if board[i][j] == 1:
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                    danger.add(tuple([nx, ny]))

    return len(danger)


if __name__ == '__main__':
    print(other_solution_1([[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
    print(other_solution_1([[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]))
    print(other_solution_1([[0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 0, 0]]))
    print(other_solution_1([[0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0]]))

