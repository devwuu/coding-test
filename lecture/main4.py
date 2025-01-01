from collections import deque

# 시간복잡도 O(k)
def other_solution_2(nums, k):
    answer = deque(nums)
    answer.rotate(-k) # 시간복잡도 O(k)
    return list(answer)


# 시간복잡도 O(k)
def other_solution_1(nums, k):
    answer = deque(nums)

    for i in range(k): # 시간복잡도 O(k)
        letter = answer.popleft() # 덱은 연결리스트라서 O(1) 시간 복잡도를 가짐, 그냥 리스트로 두고 옮기면 O(n)이 됨(요소가 이동해서)
        answer.append(letter)

    return list(answer)



# 시간복잡도 O(len(nums))
def my_solution_1(nums, k):
    reverse = []
    answer = []

    for i in range(len(nums)):
        if i < k :
            reverse.append(nums[i])
        else:
            answer.append(nums[i])

    return answer + reverse


if __name__ == '__main__':
    print(my_solution_1([3, 7, 1, 5, 9, 2, 8], 3))
    print(my_solution_1([2, 12, 2, 1, 3, 3, 9], 2))
    print(my_solution_1([1, 2, 5, 4, 6, 7, 9], 6))
    print(my_solution_1([1, 3, 6, 8, 14, 2, 1, 7], 5))


