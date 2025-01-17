from collections import defaultdict

# two pointers
def other_solution_1(nums, target):

    left = 0
    right = len(nums) - 1
    nums.sort() # o(nlogn)

    while left < right : #o(n), 두 인덱스가 같거나 역전되는 순간 모든 요소에 대한 탐색이 완료된 갓
        add = nums[left] + nums[right]
        if add == target:
            return [nums[left], nums[right]]
        elif add > target:
            right -= 1
        else:
            left += 1

    return [0] * 2

def my_solution_1(nums, target):
    dic = defaultdict(int)
    for x in nums: # o(n)
        y = target - x
        if y in dic : # o(n)
            return sorted([x, y])
        else:
            dic[x] = 1

    return [0] * 2


if __name__ == '__main__':
    print(other_solution_1([3, 7, 2, 12, 9, 15, 8, 11], 12))
    print(other_solution_1([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
    print(other_solution_1([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
    print(other_solution_1([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
    print(other_solution_1([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
    print(other_solution_1([7, 5, 12, 20], 15))

