def my_solution_1(score, k):
    answer = 0

    for s in score:
        if s >= k:
            answer += 1

    return answer


if __name__ == '__main__':
    print(my_solution_1([60, 50, 80, 90, 55, 70, 65, 45], 60))
    print(my_solution_1([10, 20, 30, 40, 50], 60))
    print(my_solution_1([50, 65, 75, 87, 90, 55, 78, 93, 100], 70))
    print(my_solution_1([99, 30, 50, 55, 68, 70, 90, 100], 80))


