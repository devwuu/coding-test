from collections import defaultdict

# dictionary 에서 데이터를 가져올 때는 o(1) 임을 이용
# o(n)
def other_solution_1(nums, target):
    answer = [0] * 2
    table = defaultdict(int)

    for x in nums: # o(n)
        y = target - x # 해가 1개이기 때문에 여러가지 case 를 고려할 필요가 없음
        if y in table : # o(1)
            return sorted([x, y])
        table[x] = 1

    return answer


if __name__ == '__main__':
    print(other_solution_1([3, 7, 2, 12, 9, 15, 8], 12))
    print(other_solution_1([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
    print(other_solution_1([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
    print(other_solution_1([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
    print(other_solution_1([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
    print(other_solution_1([7, 5, 12, 20], 15))
