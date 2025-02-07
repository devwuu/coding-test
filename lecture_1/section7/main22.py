def other_solution_1(box, limit):
    answer = 0
    left = limit

    box.sort(key = lambda v : -v[1])

    for b in box:
        if left <= 0:
            return answer
        answer += b[1] * min(left, b[0]) # 실을 수 있는 남은 상자 갯수와 원래 상자 갯수 중 작은 상자 갯수만큼 싣는다
        left -= min(left, b[0])
    return answer

def my_solution_1(box, limit):
    answer = 0
    idx = 0

    box.sort(key = lambda v : -v[1])

    for i in range(0, limit):
        if box[idx][0] == 0:
            idx += 1
        answer += box[idx][1]
        box[idx][0] -= 1

    return answer


if __name__ == '__main__':
    print(other_solution_1([[2, 20], [2, 10], [3, 15], [2, 30]], 5))
    print(other_solution_1([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10))
    print(other_solution_1([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15))
    print(other_solution_1([[2, 70], [5, 100], [3, 90], [1, 95]], 8))
    print(other_solution_1([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500))

