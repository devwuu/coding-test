
def my_solution_1(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c: # stack[-1] : 제일 위에 있는 요소 가져오기
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)


if __name__ == '__main__':
    print(my_solution_1("acbbcaa"))
    print(my_solution_1("bacccaba"))
    print(my_solution_1("aabaababbaa"))
    print(my_solution_1("bcaacccbaabccabbaa"))
    print(my_solution_1("cacaabbc"))


