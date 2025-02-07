
def my_solution_1(n):
    if n != 1:
        return n * my_solution_1(n-1)
    return n


if __name__ == '__main__':
    print(my_solution_1(5))
    print(my_solution_1(6))
    print(my_solution_1(7))
    print(my_solution_1(8))

