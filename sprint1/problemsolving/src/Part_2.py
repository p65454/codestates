"""
Bare Minimum Requirements
유기적으로 연결되는 파이썬 코드와 추상적인 숫자에 익숙해집니다.

요구사항:
    우리는 지금까지 다양한 코딩을 진행해왔습니다.
    코딩을 뛰어넘어 생각하는 프로그래밍을 해야 데이터 직군뿐만아니라 직업인으로서 
    문제를 찾고 더 나은 방향을 모색할 수 있습니다.
    문제를 해결하고 더 나은 방법을 연구해보는 것은 여러분들을 위한 중요한 수행입니다.

    '리스트의 값 중 최댓값'을 구하도록 코드를 구현하세요.
    파이썬의 내장함수를 사용하지 않고, 반복문과 조건문을 활용합니다.
    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    입력값:
        [4, 8, 5, 11, 7, 2]
    출력값:
        11
"""

def part2(num):
    max = num[0]
    for i in num:
        if i > max:
            max = i
    return max

