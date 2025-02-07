

cnt = 0
def other_solution_1(n, edges):
    adj = [[0] * (n+1) for _ in range(n+1)]
    visited = [0] * (n + 1)

    for [e1, e2] in edges: # 인접 행렬
        adj[e1][e2] = 1
        adj[e2][e1] = 1
    global cnt
    cnt = 0 # !! 글로벌 변수는 꼭 사용 전에 초기화 해줘야 이전 실행에 영향을 받지 않음 !!
    DFS(1, adj, visited, n) # 행 탐색을 한다. 그래프에서 n번 노드에 연결된 노드는 n행을 보면 알 수 있음(m행값이 1이면 인접한 것)

    return n - cnt


def DFS(i, adj, visited, n):
    global cnt
    cnt += 1
    visited[i] = 1
    for j in range(1, n+1): # 행 탐색을 한다. 그래프에서 n번 노드에 연결된 노드는 n행을 보면 알 수 있음(m행값이 1이면 인접한 것)
                            # 열 탐색은 할 필요가 없음.
        if adj[i][j] == 1 and visited[j] == 0:
            DFS(j, adj, visited, n)




def my_solution_1(n, edges):
    answer = 0
    connected = [0] * (n + 1)

    for [e1, e2] in edges:
        if e1 == 1:
            connected[e2] = 1
        if connected[e1] == 1 or connected[e2] == 1:
            connected[e1] = connected[e2]  = 1

    for c in connected:
        if c == 0:
            answer += 1

    return answer - 1


if __name__ == '__main__':
    print(other_solution_1(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
    print(other_solution_1(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
    print(other_solution_1(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
    print(other_solution_1(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))
