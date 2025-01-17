
# o(n)
def my_solution_1(nums):
    x = y = 0 # x: 행, y: 열
    d = {"R":[0, 1], "L":[0, -1], "U":[-1, 0], "D": [1, 0]} # o번 idx : 행, 1번 idx: 열
    # moves = list(nums)
    for m in nums: # o(n)
        x += d[m][0] # 격자판을 벗어나지 않는 명령만 주어지기 때문에 idx 검증하지 않음
        y += d[m][1]
    return [x, y]


if __name__ == '__main__':
    print(my_solution_1('RRRDDDLU'))
    print(my_solution_1('DDDRRRDDLL'))
    print(my_solution_1('RRRRRRDDDDDDUULLL'))
    print(my_solution_1('RRRRDDDRRDDLLUU'))
