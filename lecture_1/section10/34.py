def other_solution_1(n):
    if n == 1 or n == 2 :  # 피보나치 수열 기초값
        return 1
    else:
        return other_solution_1(n-1) + other_solution_1(n-2)

# 피보나치 : f(n) = f(n-1) + f(n-2)
def my_solution_1(n):
    if n == 0: # n-2 최소값
        return 0
    elif n == 1 :  # n-1 최소값
        return 1
    else:
        return my_solution_1(n-1) + my_solution_1(n-2)

if __name__ == '__main__':
    print(my_solution_1(5))
    print(my_solution_1(6))
    print(my_solution_1(8))
    print(my_solution_1(10))

