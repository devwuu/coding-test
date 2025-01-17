def my_solution_1(nums):
    answer = 0
    length = 0

    for n in nums:
        if n == 1:
            length += 1
        else:
            answer = max(answer, length)
            length = 0

    answer = max(answer, length)

    return answer


if __name__ == '__main__':
    print(my_solution_1([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
    print(my_solution_1([0, 0, 1, 0, 1, 0, 0]))
    print(my_solution_1([1, 1, 1, 1, 1]))
    print(my_solution_1([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))


