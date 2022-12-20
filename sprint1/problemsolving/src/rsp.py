"""
Extra Requirements
가위바위보 게임을 구현해주세요! 기초 코드는 유어클래스 노트를 참고해주세요.
아래 문제는 점수에 들어가지 않습니다. 자유롭게 도전해주세요.
아래 코드를 활용하고, 설명을 참고하여 기초 기능을 구현해보세요.
추가 기능 구현은 아래에 제시된 것을 참고하거나 본인만의 아이디어로 구현해보세요!

기초 기능:
    - 게임 시작시 환영 메세지 출력하기
    - 사용자 입력을 직접 받고, 컴퓨터는 자동으로 랜덤으로 가위바위보 실행하기
        - 사용자가 지정된 값 이외의 값을 입력할 시 재입력 받기
    - 사용자와 컴퓨터 결과 비교해서 사용자의 스코어 업데이트하기
    - 게임 종료시 스코어 결과 보여주기
추가 기능:
    - 사용자가 아닌 유저 이름을 입력받아 출력해주기
    - 가위바위보 시각화하기
    - 승패의 결과를 유저가 보고 누가 이겼는지 올바른 입력을 받아 입력받는데 까지 걸린 시간 평균내서 출력해주기

(참고사항)
pass 안에는 값이 들어가지 않을 수 있고 들어가야될 수도 있습니다.
상황에 적절하게 수정해주세요.
"""

def rock_sciss_paper():
    # 메시지 모음
    welcome_message = "[ 가위바위보 게임을 시작합니다. 게임 종료를 원하시면 게임종료 또는 9를 입력해주세요! ]"
    win_message = "********** 사용자가 이겼습니다. **********"
    loss_message = "********** 사용자가 졌습니다. **********"
    tie_message = "********** 무승부입니다. **********"
    quit_message = "********** 게임을 종료합니다. **********"
    # 딕셔너리 모음
    choice_options = {
        '1': "가위",
        '2': "바위",
        '3': "보",
        '9': "게임종료"
    }
    score = {
        "사용자승": 0,
        "무승부": 0,
        "사용자패": 0
    }

    def show_welcome_message():
        print(welcome_message)


    def get_user_choice(pass):
        pass


    def quit_game(pass):
        print(quit_message)


    def compare_choices_and_get_result(pass):
        pass


    def display_result_message_and_update_score(pass):
        pass
    

    # 게임 시작
    show_welcome_message()
    while user_choice != "게임종료":
        pass

    print('')
    quit_game(pass)


if __name__ == "__main__":
    rock_sciss_paper()