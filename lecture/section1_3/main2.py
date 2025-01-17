def my_solution_1(nums):
    idx = 0
    answer = nums[idx]

    for i in range(len(nums)):
        if answer > nums[i]:
            idx = i
            answer = nums[i]

    return idx


if __name__ == '__main__':
    print(my_solution_1([7, 10, 5, 3, 2, 15, 19]))
    print(my_solution_1([-12, 12, 30, -15, -5, 3, 9, -11, 14]))


