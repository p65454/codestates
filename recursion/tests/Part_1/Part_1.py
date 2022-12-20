import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import oneto100, recursion_advanced
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_oneto100_return_correct_answer():
    from src.Part_1 import oneto100

    assert oneto100(10) == 55, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert oneto100(20) == 210, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert oneto100(30) == 465, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert oneto100(50) == 1275, "어떤 수를 넣어도 정확한 값을 반환해야합니다."
    assert oneto100(100) == 5050, "어떤 수를 넣어도 정확한 값을 반환해야합니다."


def test_oneto100_is_recursion():
    from src.Part_1 import oneto100

    assert oneto100.cnt > 200, "재귀함수로 문제를 해결해주세요!"

def test_recursion_advanced_working_normally():
    from src.Part_1 import recursion_advanced

    test_sentence = 'testing...'
    assert (recursion_advanced(test_sentence) == '...gnitset')
    
    test_sentence = 'Codestates'
    assert (recursion_advanced(test_sentence) == 'setatsedoC')
    
    test_sentence = 'Recursion'
    assert (recursion_advanced(test_sentence) == 'noisruceR')

def test_recursion_advanced_is_recursion():
    from src.Part_1 import recursion_advanced

    print(recursion_advanced.cnt)
    assert recursion_advanced.cnt >= 29, '재귀함수로 문제를 해결해야합니다.'
