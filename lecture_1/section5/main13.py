
# 가장자리는 무조건 원소보다 크기때문에 비교할 필요 없음. 주어진 배열 내에서만 확인하면 됨
def other_solution_1(nums):
    cnt = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(nums)

    for i in range(0, n):
        for j in range(0, n):
            m = nums[i][j]
            flag = True
            for d in range(0, 4):
                if 0 <= i + dx[d] < n and 0 <= j + dy[d] < n and nums[i + dx[d]][j + dy[d]] <= m:
                    flag = False
                    break
            if flag:
                cnt += 1
    return cnt

# o(n^3)
# 10 * 10 * 4 최대 400번 순회
def my_solution_1(nums):
    cnt = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(nums)

    for i in range(0, n):
        for j in range(0, n):
            m = nums[i][j]
            flag = True
            for d in range(0, 4):
                if 0 <= i + dx[d] < n and 0 <= j + dy[d] < n:
                    t = nums[i + dx[d]][j + dy[d]]
                    flag = flag and t > m # 하나라도 나(m)보다 작으면 웅덩이가 아님
            cnt = cnt + 1 if flag == True else cnt
    return cnt


if __name__ == '__main__':
    print(my_solution_1(
        [[10, 20, 50, 30, 20], [20, 30, 50, 70, 90], [10, 15, 25, 80, 35], [25, 35, 40, 55, 80], [30, 20, 35, 40, 90]]))
    print(my_solution_1(
        [[80, 25, 10, 65, 100], [20, 10, 32, 70, 33], [45, 10, 88, 9, 90], [10, 35, 10, 55, 66], [10, 84, 65, 88, 99]]))
    print(my_solution_1(
        [[33, 22, 55, 65, 55], [55, 88, 99, 12, 19], [18, 33, 25, 57, 77], [46, 78, 54, 55, 99], [33, 25, 47, 85, 17]]))
