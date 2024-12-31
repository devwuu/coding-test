
# list 를 사용한 방법 -- direct address table
def solution2(nums):
    table = [0] * 1001 # 문제에서 배열의 길이는 1000까지 올 수 있다고 주어짐, 1000까지는 길이가 길지 않아서 이렇게 풀어도 됨, 배열의 요소들도 값이 작음
                        # index를 이용한 직접 접근이 key를 이용한 접근보다 성능이 좋을 수 있음

    for num in nums: # log(n)
        table[num] += 1

    for idx in range(1000, 0, -1): # log(n)
        if table[idx] == 1:
            return idx

    return -1


# dictionary 를 사용한 방법 - hash table
def solution(nums):
    answer = -1

    table = dict()

    for num in nums:
        table[num] = 1 if table.get(num) is None else table[num] + 1

    for key, value in table.items():
        if value == 1:
            answer = max(key, answer)

    return answer


if __name__ == '__main__':
    print(solution2([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
    print(solution2([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 8]))
    print(solution2([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
    print(solution2([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
    print(solution2([1, 3, 1, 5, 7, 2, 3, 1, 5]))


