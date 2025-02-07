from collections import Counter

# o(nlogn) 또는 o(n)으로 문제 풀이
def my_solution_1(nums):
    answer = 9999999 # 원소는 최대 1,000,000까지
    cnt = Counter(nums) # o(n)
    for key, value in cnt.items(): # 최대 o(n)
        if key == value:
            answer = min(answer, key)

    return answer if answer < 9999999 else -1


if __name__ == '__main__':
    print(my_solution_1([1, 2, 3, 1, 3, 3, 2, 4]))
    print(my_solution_1([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
    print(my_solution_1([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
    print(my_solution_1([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
    print(my_solution_1(
        [11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12])
    )


