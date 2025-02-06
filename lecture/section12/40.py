

cnt = 0
def my_solution_1(n, edges):

    visited = [0] * (n+1)
    adj = [[] * (n+1) for _ in range(n+1)]

    for [e1, e2] in edges: # 인접 리스트
        adj[e1].append(e2)
        adj[e2].append(e1)

    global cnt
    cnt = 0
    BFS(1, adj, visited)

    return n - cnt


def BFS(i, adj, visited):
    global cnt
    cnt += 1
    visited[i] = 1

    for j in adj[i]: # 인접 리스트에 담긴 것이 연결된 노드 번호임
        if visited[j] == 0:
            BFS(j, adj, visited)





if __name__ == '__main__':
    print(my_solution_1(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
    print(my_solution_1(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
    print(my_solution_1(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
    print(my_solution_1(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))


