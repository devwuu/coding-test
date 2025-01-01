from collections import Counter
import math


def other_solution_1(s):

    str = Counter(s)
    odd = 0
    length = len(s)
    for key, value in str.items():
        if value % 2 == 1:
            odd += 1

    return length - odd + 1 if odd > 0 else length # 홀수 글자 : 나머지(1글자)만 빼고 모든 글자 사용, 단, 1개 추가 ( 중앙에 놓을 글자 )


def my_solution_2(s):

    str = Counter(s)
    odd = 0
    length = 0
    for key, value in str.items():
        if value % 2 == 1:
            odd += 1
        length += math.floor(value / 2) * 2

    return length +1 if odd > 0 else length


# 팰린드롬?
# 순방향으로 읽을 때, 역방향으로 읽을 때 모두 같은 문자열이 되는 문자열

def my_solution_1(s):

    str = Counter(s)
    odd = 0
    length = 0
    for key, value in str.items():
        if value % 2 == 1:
            odd += 1
            length += math.floor(value / 2) * 2
        else:
            length += value

    return length +1 if odd > 0 else length


if __name__ == '__main__':
    print(other_solution_1("abcbbbccaaeee"))
    print(other_solution_1("aabbccddee"))
    print(other_solution_1("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
    print(other_solution_1("aabcefagcefbcabbcc"))
    print(other_solution_1("abcbbbccaa"))
