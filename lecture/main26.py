from bisect import bisect_left

def other_solution_1(nums, weight):
    left = 0
    right = len(nums)

    while left < right :
        mid = (left + right)//2
        if nums[mid] < weight:
            left = mid + 1 # 작은 값은 건너뛰기(버리기)
        else:
            right = mid # 해당하는 값은 right가 가리키게 한다, 즉, 조건에 맞는 값을 찾았을 때만 right가 움직인다

    return right if right != len(nums) else -1


def my_solution_1(nums, weight):
    idx = bisect_left(nums, weight) # o(logn) 이진탐색, lower bound
    return -1 if idx == len(nums) else idx



if __name__ == '__main__':
    print(other_solution_1([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))
    print(other_solution_1([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
    print(other_solution_1([50, 55, 60, 65, 70, 80, 80, 80, 80, 90, 90, 90], 80))
    print(other_solution_1([20, 30, 40, 50, 60, 70], 90))
    print(other_solution_1([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))


