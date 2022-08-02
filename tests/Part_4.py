# """
# Part 4
# """

# import os
# from src import Part_4

# def test_adv_conda():
#     assert Part_4.VIRTUAL_ENV_LIST in {"conda env list > result.txt",
#                                         "conda env list >> result.txt"}

# def test_adv_branch():
#     '''
#     1) 수강생의 과제 파일 안에 브랜치 목록이 있는지 확인합니다.
#     2) 브랜치 목록에 git-branch 와 origin/git-merge 가 있는지 확인합니다.
#     '''
#     exist = False
#     FILEPATH = os.getcwd()
#     with open(FILEPATH+"/result2.txt", 'r') as file:
#         line = file.read()
#         for branch in ['git-branch', 'origin/git-merge']:
#             if branch not in line:
#                 assert exist

# def test_adv_pr_git_branch():
#     '''
#     1) 수강생이 git-branch 브랜치를 원격에 push 할 수 있는지 확인합니다.
#     2) 브랜치 목록에 origin/git-branch 와 origin/git-merge 가 있는지 확인합니다.
#     '''
#     exist = False
#     FILEPATH = os.getcwd()
#     with open(FILEPATH+"/result3.txt", 'r') as file:
#         line = file.read()
#         for branch in ['origin/git-branch', 'origin/git-merge']:
#             if branch not in line:
#                 assert exist