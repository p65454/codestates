"""
Bare Minimum Requirements
정렬을 구현하며 반복문과 조건문의 흐름을 파악합니다.

요구사항:
    정렬은 대부분의 상황에서 활용되는 대표적인 개념입니다.
    프로그래밍의 반복문과 조건문의 중요성을 다시 한 번 상기하면서 정렬이라는 목적을 달성해봅니다.
    정렬 개념을 적용하여 소스코드를 작성해주세요.

    파이썬에서 제공되는 sort와 같은 내장함수를 사용하면 안됩니다.
    반복문과 조건문만을 활용하여 구현하시길 바랍니다.
"""

def bubble_sort(li):
    """
    # 문제 1.
        거품정렬을 구현해주세요.
        매개변수로 들어온 리스트를 오름차순으로 정렬해주세요.
        단 매개변수로 들어오는 요소는 전부 정수입니다. 

        ex)
            li = [54, 26, 93, 17, 77, 31]
            bubble_sort(li)
            print(li) # [17, 26, 31, 54, 77, 93]
    """
    length = len(li)-1
    # 외부 반복문(리스트 전체를 돈다):
    for i in range(length):
        
        # 내부 반복문(값을 비교해서 swap):
        for j in range(length - i):
            # if 현재 노드 값이 뒤에 있는 노드의 값보다 큰 경우:
            if li[j] > li[j+1]:
                # swap
                li[j], li[j+1] = li[j+1], li[j]
            # if 그렇지 않으면
                # pass
    return print(li)


def insertion_sort(li):
    """
    # 문제 2.
        삽입정렬을 구현해주세요.
        매개변수로 들어온 리스트를 오름차순으로 정렬해주세요.
        단 매개변수로 들어오는 요소는 전부 정수입니다. 

        ex)
            li = [54, 26, 93, 17, 77, 31]
            insertion_sort(li)
            print(li) # [17, 26, 31, 54, 77, 93]
    """
    length = len(li)
    for i in range(1, length):
        # 이전 값들을 돌며 추출한 값과 비교:
        for j in range(i):
            # 추출한 값이 더 큰 경우:
            if li[i] > li[j]:
                # 지나감
                pass
            # 추출한 값이 더 작은 경우:
            else:
                # swap
                li[i], li[j] = li[j], li[i]

    return print(li)


def selection_sort(li):
    """
    # 문제 3.
        선택정렬을 구현해주세요.
        매개변수로 들어온 리스트를 오름차순으로 정렬해주세요.
        단 매개변수로 들어오는 요소는 전부 정수입니다. 

        ex)
            li = [54, 26, 93, 17, 77, 31]
            selection_sort(li)
            print(li) # [17, 26, 31, 54, 77, 93]
    """
    length = len(li)
    for i in range(length-1):
        # 가장 작은 노드가 저장되는 변수
        min_idx = i
        # 탐색값의 뒤 리스트를 돈다. (반복):
        for j in range(i+1, length):
            # (최소값 찾는 알고리즘)
            # 가장 작은 노드보다 현재 노드 값이 더 작으면
            if li[j] < li[min_idx]:
                # 가장 작은 값의 인덱스 바뀐다.
                min_idx = j
        # swap
        li[min_idx], li[i] = li[i], li[min_idx]
    return li
