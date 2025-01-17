
def other_solution_1(nums): # o(logn)
                            # 배열이 오름차순 정렬되어 있고 중복되는 요소가 없기 때문에 고정된 숫자를 만들어낼 수 없어짐 --> 다 버리고 탐색 재시작
    left = 0
    right = len(nums)

    while left <= right:
        mid = (left + right)//2
        if nums[mid] < mid:
            left = mid + 1
        elif nums[mid] > mid:
            right = mid - 1
        else:
            return mid

    return -1


def my_solution_1(nums): # o(n)

    for i in range(len(nums)):
        if i == nums[i]:
            return i

    return -1



if __name__ == '__main__':
    print(other_solution_1([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
    print(other_solution_1([-10, -5, -2, 3, 4, 6, 7, 8]))
    print(other_solution_1([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(other_solution_1([-5, -3, 0, 1, 2, 3, 4, 7]))
    print(other_solution_1([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


