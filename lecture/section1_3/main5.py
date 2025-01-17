from collections import deque

# 시간복잡도 O(n)
def other_solution_2(nums):
    answer = deque()
    answer.appendleft(nums[0])
    for i in range(1, len(nums)): # 시간복잡도 O(n)
        if nums[i-1] != nums[i]:
            answer.appendleft(nums[i]) #시간복잡도 O(1)
    return list(answer)

# 시간복잡도 O(n)
def other_solution_1(nums):
    prev = 999999
    answer = deque()
    for num in nums: # 시간복잡도 O(n)
        if prev != num:
            answer.appendleft(num) #시간복잡도 O(1)
        prev = num
    return list(answer)

# 시간복잡도 O(n)
def my_solution_2(nums):
    distinct = deque(set(nums))
    answer = deque()
    for i in range(len(distinct)): # 시간복잡도 O(n)
        num = distinct.pop()
        answer.append(num) #시간복잡도 O(1)
    return list(answer)

# 시간복잡도 O(nlogn)
def my_solution_1(nums):
    distinct = set(nums)
    answer = list(distinct)
    answer.sort(reverse=True)
    return answer



if __name__ == '__main__':
    print(other_solution_2([0, 1, 1, 1, 2, 2, 2, 3]))
    print(other_solution_2([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
    print(other_solution_2([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
    print(other_solution_2([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))


