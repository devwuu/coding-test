from collections import deque

def my_solution_1(nums):
    dq = deque(nums)

    while dq:
        if len(dq) < 3: # 마지막 작업턴이 되는 경우
            return dq[-1] # 제일 마지막 요소 retrun
        else:
            dq.popleft()
            dq.popleft()
            third = dq.popleft()
            dq.append(third)


if __name__ == '__main__':
    print(my_solution_1([3, 1, 4, 5, 2, 6, 7]))
    print(my_solution_1([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
    print(my_solution_1([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
    print(my_solution_1([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
    print(my_solution_1([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))



