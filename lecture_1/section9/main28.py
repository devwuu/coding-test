
def my_solution_2(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return "NO"
            stack.pop()

    return "YES" if len(stack) == 0 else "NO"


def my_solution_1(s):
    stack = []
    try:
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                stack.pop()
    except IndexError:
        return "NO"

    return "YES" if len(stack) == 0 else "NO"


if __name__ == '__main__':
    print(my_solution_2("((()))()"))
    print(my_solution_2("(()(()"))
    print(my_solution_2("()())"))
    print(my_solution_2("())("))
    print(my_solution_2("((())))()("))



