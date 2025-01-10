
def my_solution_1(weight, limit):
    answer = 0
    total = 0

    weight.sort() # o(nlogn)

    for w in weight: # o(n)
        if total + w > limit:
            return answer
        total += w
        answer += 1

if __name__ == '__main__':
    print(my_solution_1([300, 100, 230, 120, 90, 150, 60], 700))
    print(my_solution_1([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
    print(my_solution_1([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
    print(my_solution_1([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
    print(my_solution_1([100, 110, 50, 50, 60, 70, 50, 55, 57], 350))

