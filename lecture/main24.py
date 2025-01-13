def other_solution_2(nums, k): # o(n) 슬라이딩 윈도우 기법
    total = sum(nums) # o(n)
    wn = len(nums) - k # window의 크기 => 사용하는 숫자 빼고 나머지 숫자들이 window가 된다
    wn_score = 0 # window의 합

    for i in range(wn):
        wn_score += nums[i]

    minimum = wn_score
    left = 0
    for right in range(wn, len(nums)): # window를 하나씩 오른쪽으로 옮긴다.
        wn_score += (nums[right] - nums[left]) # window를 옮기면 제일 왼쪽 값은 빠지고 오른쪽 값은 들어온다
        left += 1
        minimum = min(minimum, wn_score) # 총계에서 가장 작은 윈도우 값을 빼면 가장 큰 연속 수열 값이 나옴

    return total - minimum


def other_solution_1(nums, k): # o(n^2)
    answer = 0
    n = len(nums)

    for i in range(k+1): # 경우의 수 : 왼쪽에서 0개 ~ k개 뽑은 경우, 오른쪽에서 나머지 뽑는 경우 => k+1 case(0~k)
        add = 0
        for j in range(i): # 왼쪽에서부터 j 개
            add += nums[j]
        for l in range(n-k+i, n): # 오른쪽에서부터 l개, deque를 사용하면 반복문 돌 때마다 뽑아지기 때문에 idx로 접근
            add += nums[l]
        answer = max(answer, add)

    return answer



if __name__ == '__main__':
    print(other_solution_2([2, 3, 7, 1, 2, 1, 5], 4))
    print(other_solution_2([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
    print(other_solution_2([1, 30, 3, 5, 6, 7], 3))
    print(other_solution_2([1, 2, 15, 3, 6, 7, 8, 9], 5))
    print(other_solution_2([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))

