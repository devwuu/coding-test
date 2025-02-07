from collections import Counter

# 팰린드롬?
# 순방향으로 읽을 때, 역방향으로 읽을 때 모두 같은 문자열이 되는 문자열

def my_solution_1(s):

    splited = Counter(s) # o(n)

    odd = 0
    for key, value in splited.items(): # o(n)
        if value % 2 == 1:
            odd += 1
            if odd > 1:
                return False

    return True


if __name__ == '__main__':
    print(my_solution_1("abacbaa"))
    print(my_solution_1("abaaceeffkckbaa"))
    print(my_solution_1("abcabbcc"))
    print(my_solution_1("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
    print(my_solution_1("aabcefagcefbcabbcc"))
