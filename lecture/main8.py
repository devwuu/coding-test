from collections import defaultdict, Counter # 기본값 타입을 정할 수 있는 dictionary

# counter를 사용하는 방법
def solution2(nums):
    answer = -1
    cnt = Counter(nums) # 배열의 원소들의 빈도수를 카운트해줌, dictionary 의 확장형
    for key, item in cnt.items():
        if item == 1:
            answer = max(key, answer)
    return answer


# dictionary 를 사용한 방법 - hash table
def solution(nums):
    answer = -1
    dic = defaultdict(int) # 기본값이 int값(0)인 dictionary
    for num in nums:
        dic[num] += 1

    for key, item in dic.items():
        if item == 1:
            answer = max(key, answer)

    return answer


if __name__ == '__main__':
    print(solution2([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
    print(solution2([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 8]))
    print(solution2([2235253, 5525612, 142561567, 123456789, 2235253, 560, 123456789, 142561567]))
    print(solution2([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
    print(solution2([1, 3, 1, 5, 7, 2, 3, 1, 5]))


