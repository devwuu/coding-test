from collections import deque

def other_solution_1(board):
    answer = 0

    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                BFS(board, i, j)
                answer += 1 # 하나의 트리(영역)가 순회 완료되었으니 count 를 올려준다

    return answer

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

## 노드 == 행X열 자리. 즉 이어진 영역 하나 하나가 하나의 트리라고 보는 관점
def BFS(board, i, j):
    dq = deque()
    dq.append([i, j]) # 최초 노드
    while dq: # 더이상 방문할 노드가 없을 때까지 반복 -> 이 반복이 끝나면 하나의 트리(영역)을 순회 완료한 것
        x, y = dq.popleft()
        board[x][y] = 0 # 방문 완료된 자리는 체크 (무한 방문 방지)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] == 1:
                dq.append([nx, ny]) # 다음번에 방문할 노드를 넣어준다



if __name__ == '__main__':
    print(other_solution_1([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
    print(other_solution_1([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
    print(other_solution_1([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
    print(other_solution_1([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

