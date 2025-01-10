def other_solution_1(m, nums):
    answer = 0

    nums.sort(key = lambda v : v[0])
    start = end = i = 0
    n = len(nums)

    while i < n: # 모든 요소를 전체 탐색
        while i < n and nums[i][0] <= start: # 라인의 시작점이 기준점과 겹칠 경우 라인 종료 지점 탐색 시작, start 지점이 m과 동일해지기 때문에 i값 검증하지 않으면 무한정 루프하여 인덱스아웃바운드 에러가 발생할 것임
            end = max(end, nums[i][1]) # 가장 멀리서 종료되는 선 선택
            i += 1 # 배열의 모든 요소 탐색, 시작점이 순차적으로 정렬되어 있기 때문에 start의 크기와 i의 크기가 비례하게 됨 -> 즉, i가 n이 되어 종료되는 시점은 start 지점에 m에 도달하는 지점이다
        # 첫번째 반복문에서 무조건 1개의 선(가장 멀리 가는 선)은 선택될 것임, 이 선을 사용한다고 하고 cnt 값 증가 시킴
        answer += 1
        if end == m:
            return answer
        start = end

if __name__ == '__main__':
    print(other_solution_1(12, [[5, 10], [1, 8], [0, 2], [0, 3], [2, 5], [2, 6], [10, 12], [7, 12]]))
    print(other_solution_1(15, [[1, 10], [0, 8], [0, 7], [0, 10], [12, 5], [0, 12], [8, 15], [5, 14]]))
    print(other_solution_1(20, [[3, 7], [5, 8], [15, 20], [0, 5], [7, 14], [3, 10], [0, 8], [13, 18], [5, 9]]))
    print(other_solution_1(30, [[5, 7], [3, 9], [2, 7], [0, 1], [0, 2], [0, 3], [19, 30], [8, 15], [7, 12], [13, 20]]))
    print(other_solution_1(25, [[10, 15], [15, 20], [5, 15], [3, 16], [0, 5], [0, 3], [12, 25]]))
