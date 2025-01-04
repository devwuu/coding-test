def other_solution_1(moves):
    x = y = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0

    for m in moves: # o(n)
        if m == 'R':
            idx += 1
        elif m == 'L':
            idx += 3 # 왼쪽으로 90도 도는 것 == 오른쪽으로 270도 도는 것
        else:
            cur = idx % 4
            x += dx[cur]
            y += dy[cur]

    return [x, y]

def my_solution_2(moves):
    x = y = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0

    for m in moves: # o(n)
        if m == 'R':
            idx += 1
        elif m == 'L':
            idx -= 1
        else:
            cur = idx % 4
            x += dx[cur]
            y += dy[cur]

    return [x, y]

def my_solution_1(moves):
    x = y = 0
    dic = {"3":[0,1], "12":[-1,0], "9": [0, -1], "6": [1, 0]}
    turn = ["3", "6", "9", "12"]
    idx = 0

    for m in moves: # o(n)
        if m == 'R':
            idx += 1
        elif m == 'L':
            idx -= 1
        else:
            cur = idx % 4 # 현재 보고 있는 방향 확인, 나머지 연산자 사용하면 원형으로 사용 가능
            x += dic[turn[cur]][0]
            y += dic[turn[cur]][1]

    return [x, y]


if __name__ == '__main__':
    print(other_solution_1('GGGRGGG'))
    print(other_solution_1('GGRGGG'))
    print(other_solution_1('GGGGGGGRGGGRGGRGGGLGGG'))
    print(other_solution_1('GGLLLGLGGG'))

