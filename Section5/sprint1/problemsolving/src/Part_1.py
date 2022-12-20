"""
Bare Minimum Requirements

파이썬의 기본형태를 이해하고 컴프리헨션을 활용할 줄 알아야 합니다.

요구사항:
    반복해서 수학적인 개념이 접목된 프로그래밍 문제를 해결해봅니다.
    프로그래밍에 익숙해지는 과정에는 코드 자체에 대한 맥락을 읽어야 하는 것이 중요합니다.

    리스트 컴프리헨션 개념을 적용하여 '1~100까지 7과 5의 공배수' 를 구하는 코드를 작성하세요.
    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    입력값:
        없음
    출력값:
        [35, 70]
"""

def part1():

    ##### 소스코드를 작성해주세요 #####
    return [i for i in range(1,101) if i % 5 ==0 and i % 7 ==0]
