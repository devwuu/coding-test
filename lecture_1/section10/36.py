dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0
def other_solution_1(board):
    answer = []

    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == 1:
                global cnt
                cnt = 0
                other_solution_1_dfs(i, j, board)
                answer.append(cnt)

    return answer

def other_solution_1_dfs(i, j, board):
    board[i][j] = 0
    global cnt
    cnt += 1 # 호출된 시점 == 1개가 발견되었다는 의미이기 때문에 최초에 +1을 해준다
    for d in range(0, 4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] == 1:
            other_solution_1_dfs(nx, ny, board)

##########

pixel = 1
def my_solution_1(board):
    answer = []
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == 1:
                global pixel
                pixel = 1
                my_solution_1_adjoin(board, i, j)
                answer.append(pixel)

    return answer

def my_solution_1_adjoin(board, i, j):
    board[i][j] = 0
    for d in range(0, 4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] == 1:
            global pixel
            pixel += 1
            my_solution_1_adjoin(board, nx, ny)



if __name__ == '__main__':
    print(other_solution_1([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
    print(other_solution_1([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
    print(other_solution_1([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
    print(other_solution_1([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

