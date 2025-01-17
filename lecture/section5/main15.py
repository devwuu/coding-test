
# o(n)
def my_solution_1(n, nums):
    x = y = 0 # x: 행, y: 열
    d = {"R":[0, 1], "L":[0, -1], "U":[-1, 0], "D": [1, 0]} # o번 idx : 행, 1번 idx: 열
    for m in nums: # o(n)
        if 0 <= x + d[m][0] < n and 0 <= y + d[m][1] < n:
            x += d[m][0]
            y += d[m][1]
    return [x, y]


if __name__ == '__main__':
    print(my_solution_1(5, 'RRRDDDUUUUUUL'))
    print(my_solution_1(7, 'DDDRRRDDLL'))
    print(my_solution_1(5, 'RRRRRDDDDDU'))
    print(my_solution_1(6, 'RRRRDDDRRDDLLUU'))
