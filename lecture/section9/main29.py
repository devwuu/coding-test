
def my_solution_1(s):
    stack = []
    for c in s:
        if c == "#":
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack) # "구분자".join(리스트) -> 문자열 합치기


if __name__ == '__main__':
    print(my_solution_1("abc##ec#ab"))
    print(my_solution_1("kefd#ef##s##"))
    print(my_solution_1("teac#cher##er"))
    print(my_solution_1("englitk##shabcde##ff##ef##ashe####"))
    print(my_solution_1("itistime####gold"))


