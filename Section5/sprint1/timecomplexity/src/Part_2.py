"""
Bare Minimum Requirements

요구사항:
    작성되어있는 함수의 시간복잡도가 어떻게 되는지 판별할 수 있어야합니다. 

    문제로 작성된 함수를 확인하여, 해당 함수의 시간복잡도와 그 이유를 작성해주세요.
    문제로 작성된 함수 (part1_q1, part1_q2, part1_q3)는 수정하시면 안됩니다. 

    정답을 작성하는 함수내부에 답을 작성해주세요 
    (part1_q1_answer, part1_q2_answer, part1_q3_answer)

    time_complexity에는 전역으로 선언된 시간복잡도 변수를 사용해주세요.
    reason에는 그렇게 생각한 이유를 문자열로 작성해주세요.
    
"""

ANSWER = 'wrong answer'
CONSTANT = 'O(1)'
LOGARITHMIC = 'O(logn)'
LINEAR = 'O(n)'
LINEARITHMIC = 'O(nlogn)'
QUADRATIC = 'O(n^2)'
EXPONENTIAL = 'O(c^n)' 


def part2_q1(li):
    for i in li:
        print(i)

    res = []
    for i in li:
        for j in li:
            res.append(i * j)

    return res
    

def part2_q1_answer():
    time_complexity = QUADRATIC
    reason = "가장 긴 연산이 아래의 li*li연산이기때문"

    return (time_complexity, reason)


def part2_q2(li):
    for i in li:
        break


def part2_q2_answer():
    time_complexity = CONSTANT
    reason = "break로 바로 탈출되면서 1번 연산 되었기 때문"

    return (time_complexity, reason)


def part2_q3(num):
    res = 0
    cur = 1
    while (cur < num):
        res += 1
        cur = cur * 2
    return res


def part2_q3_answer():
    time_complexity = LOGARITHMIC
    reason = "반복문동안 cur이 거듭제곱되었고 그 횟수는 log(num)만큼이기 때문"

    return (time_complexity, reason)
