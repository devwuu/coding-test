
# 이진탐색 ==> o(logn)
# "정렬"되어 있는 자료구조에 사용
def other_solution_1(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right : # 두 자리가 역전되면 탐색 완료 -> 모든 요소 탐색 됨
        mid = (left + right) // 2
        if nums[mid] < target: # mid보다 큰 idx에 target이 존재
            left = mid + 1
        elif nums[mid] > target:  # mid보다 작은 idx에 target이 존재
            right = mid - 1
        else:
            return mid

    return -1

def my_solution_2(nums, target):
    try:
        return nums.index(target) # o(n)
    except:
        return -1

def my_solution_1(nums, target):
    for i in range(len(nums)): # o(n)
        if nums[i] == target:
            return i
    return -1



if __name__ == '__main__':
    print(other_solution_1([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
    print(other_solution_1([-3, 0, 2, 5, 8, 9, 12, 15], 0))
    print(other_solution_1([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
    print(other_solution_1([3, 6, 9, 12, 17, 29, 33], 3))
    print(other_solution_1([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))


