
def other_solution_1(nums):
    stack = []
    answer = 0

    for n in nums:
        if n == 1 and len(stack) > 1 and stack[-1] == 2 and stack[-2] == 1: # 제일 위의 요소, 그 다음 요소를 비교한다
            stack.pop()
            stack.pop()
            answer += 1
        else:
            stack.append(n)

    return answer


def my_solution_1(nums):
    stack = []
    mode = False
    answer = 0

    for n in nums:
        if n == 1:
            if mode:
                mode = False
                answer += 1
            else:
                stack.append(n)
        else:
            if stack:
                stack.pop()
                mode = True

    return answer


if __name__ == '__main__':
    print(other_solution_1([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
    print(other_solution_1([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
    print(other_solution_1([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
    print(other_solution_1([2, 1, 1, 1, 2, 1, 2]))
    print(other_solution_1([1, 1, 1, 1, 1, 1, 1]))


