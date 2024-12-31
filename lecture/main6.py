def solution1(nums, target):
    answer = [0] * 2
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)): # 시간복잡도 O(n^2)
            num1 = nums[i]
            num2 = nums[j]
            if num1 + num2 == target:
                answer = sorted([num1, num2]) # 오름차순 정렬
                return answer
    return answer

def solution(nums, target):
    answer = [0] * 2
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)): # 시간복잡도 O(n^2)
            num1 = nums[i]
            num2 = nums[j]
            if num1 + num2 == target:
                answer = [num1, num2] if num1 < num2  else [num2, num1]
                return answer
    return answer


# 이 문제는 O(n)으로도 풀 수 았고 O(nlogn)으로도 풀 수 있대.
# nlogn은 sort 함수 아닐지

if __name__ == '__main__':
    print(solution1([7, 9, 2, 13, 3, 15, 8, 11], 12))
    print(solution1([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
    print(solution1([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
    print(solution1([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
    print(solution1([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
    print(solution1([7, 5, 12, 20], 15))



