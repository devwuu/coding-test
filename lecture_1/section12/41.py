
def my_solution_1(n, edges):
    answer = 0

    adj = [[] * (n+1) for _ in range(n+1)]
    checked = [0] * (n+1)

    for [v1, v2] in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    for i in range(1, n+1):
        if checked[i] == 0: # 동아리 확인이 안된 사람들만 체크
            DFS(i, adj, checked)
            answer += 1

    return answer

def DFS(v, adj, checked):
    checked[v] = 1
    for nv in adj[v]:
        if checked[nv] == 0: # 동아리 확인이 안된 사람들만 체크
            DFS(nv, adj, checked)



if __name__ == '__main__':
    print(my_solution_1(10, [[1, 2], [2, 3], [1, 4], [1, 5], [6, 8], [7, 8], [9, 10]]))
    print(my_solution_1(20, [[1, 2], [2, 5], [5, 7], [9, 7], [5, 13], [15, 13], [3, 4], [4, 6], [6, 8], [8, 10], [11, 12],
                        [14, 16], [16, 17], [17, 18], [19, 20]]))
    print(my_solution_1(7, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(my_solution_1(30, [[5, 6], [6, 7]]))

