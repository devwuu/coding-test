
# o(nlogn)
def other_solution_2(nums):
    answer = []
    l = len(nums)
    nums.sort() # o(nlogn)

    mini = 9999
    for i in range(1, l): # o(n)
        diff = nums[i] - nums[i-1]
        mini = min(mini, diff)

    for i in range(1, l): # o(n)
        if nums[i] - nums[i-1] == mini :
            answer.append([nums[i-1], nums[i]])

    return answer


# o(n^2)
def other_solution_1(nums):
    answer = []
    l = len(nums)

    mini = 9999
    for i in range(0, l): # o(n^2)
        for j in range(i+1, l):
            diff = abs(nums[i] - nums[j]) # 절대값
            if diff < mini:
                mini = diff

    for i in range(0, l): # o(n^2)
        for j in range(i+1, l):
            diff = abs(nums[i] - nums[j]) # 절대값
            if diff == mini :
                answer.append(sorted([nums[i], nums[j]]))

    return answer


# o(nlogn)
def my_solution_1(nums):
    answer = []

    nums.sort() # o(nlogn)
    # 정렬했을 때 인접한 요소끼리의 차가 가장 작음

    mini = 9999
    for i in range(0, len(nums) -1): #o(n)
        a = nums[i]
        b = nums[i+1]

        if mini > (b-a):
            mini = b-a
            answer = [[a,b]]
        elif mini == (b-a):
            answer.append([a, b])

    return answer


if __name__ == '__main__':
    print(other_solution_2([3, 8, 1, 5, 12]))
    print(other_solution_2([2, 1, 3, 5, 4]))
    print(other_solution_2([5, 10, 15, 20, 25, 11]))
    print(other_solution_2([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
    print(other_solution_2([100, 200, 300, 400, 120, 130, 135, 132, 121]))

