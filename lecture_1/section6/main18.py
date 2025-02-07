from collections import Counter


def other_solution_1(nums):
    max = len(nums) // 2
    kind = len(set(nums)) # o(n), 중복을 제거하면 사탕 종류가 남음
    return min(max, kind) # 둘 중 작은 값이 먹을 수 있는 종류의 갯수가 됨

def my_solution_1(nums):
    max = len(nums) // 2
    kind = len(Counter(nums).keys()) # o(n)
    return kind if max >= kind else max


if __name__ == '__main__':
    print(other_solution_1([2, 1, 1, 3, 2, 3, 1, 2]))
    print(other_solution_1([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
    print(other_solution_1([5, 5, 5, 5, 5, 5]))
    print(other_solution_1([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
    print(other_solution_1([100, 200, 300, 400, 500, 600, 700, 800]))

