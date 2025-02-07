from collections import deque

def other_solution_1(home):
    deq = deque()
    deq.append(0)

    visited = [0] * 10_001 # 방문 노드 관리, 최대 좌표값으로 할당
    visited[0] = 1 # root 노드 방문 표시

    l = 0
    while deq:
        n = len(deq)
        for i in range(0, n): # 모든 현재 노드 탐색 완료
            v = deq.popleft()
            if v == home: # 찾던 노드인지 확인
                return l
            # 찾던 노드가 아니라면 탐색할 다음 노드(자식 노드) 확인
            for nv in [v-1, v+1, v+5]: # 현재 노드에서 이동할 수 있는 모든 자식 노드
                if 0 <= nv <= 10_000 and visited[nv] == 0: # 이미 지나온 지점(정답 지점이 아닌 경우)는 재탐색하지 않는다 -> 무한 루프 경로가 되기 때문 ( 예: 1 -> 0 -> 1 -> 0 ...)
                                                        # 주어진 노드값을 벗어나지 않게 범위 지정
                    deq.append(nv)
                    visited[nv] = 1 # 어차피 꺼내서 탐색할 것이니까 데크에 넣으면서 탐색 했다고 표시
        l += 1 # 다음 레벨(자식 노드 레벨로 이동)


def my_solution_1(home):
    answer = home // 5 # 최대한 멀리 뛰기
    etc = home % 5
    if etc == 4 : # 목적지를 넘어갔다가 되돌아오는 게 빠른 케이스
        answer += 2
    else: # 직진하는 게 빠른 케이스
        answer += etc

    return answer


if __name__ == '__main__':
    print(other_solution_1(10))
    print(other_solution_1(14))
    print(other_solution_1(25))
    print(other_solution_1(24))
    print(other_solution_1(345))

