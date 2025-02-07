dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def other_solution_1(board):
    answer = 0

    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == 1:
                answer += 1
                other_solution_1_dfs(i, j, board)

    return answer

def other_solution_1_dfs(i, j, board):
    board[i][j] = 0  # 방문 지점 체크 -> 무한 재귀 방지, dfs 함수를 호출하는 시점에서 이미 == 1 조건을 만족한 것이기 때문에 굳이 if 문 안으로 밀어넣을 필요 없음
    for d in range(0, 4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] == 1:
            other_solution_1_dfs(nx, ny, board)

#####

def my_solution_1(board):
    answer = 0

    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == 1:
                answer += 1
                board[i][j] = 2 # 방문 지점 체크 -> 무한 재귀 방지
                my_solution_1_adjoin(board, i, j)

    return answer

def my_solution_1_adjoin(board, i, j): # 최초의 영역에서 인접한 영역을 모두 2로 만들기 + 인접한 영역의 인접한 영역도 2로 만들기
    for d in range(0, 4):
        if 0 <= i + dx[d] < 5 and 0 <= j + dy[d] < 5 and board[i + dx[d]][j + dy[d]] == 1:
            board[i + dx[d]][j + dy[d]] = 2 # 방문 지점 체크 -> 무한 재귀 방지
            my_solution_1_adjoin(board, i + dx[d], j + dy[d])


if __name__ == '__main__':
    print(other_solution_1([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
    print(other_solution_1([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
    print(other_solution_1([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
    print(other_solution_1([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

