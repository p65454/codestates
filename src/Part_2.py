"""
Bare Minimum Requirements

요구사항:
    아래 문제들을 확인하며 하나씩 문제를 풀어주세요.    
"""

class Computer:
    """
    ## Computer 클래스의 코드는 수정하지 마세요 ##
    이미 완성된 코드입니다.
    아래 코드를 활용하여 문제를 해결해주세요.
    """
    def __init__(self, cpu, ram):
        self.CPU = cpu
        self.RAM = ram
        
    def browse(self):
        return('browse')

    def work(self):
        return('work')
        

class Laptop(Computer):
    """
    위에 작성된 Computer 클래스를 상속받는 Laptop 클래스를 완성해주세요. 
    """
    def __init__(self, cpu, ram, battery):
        """
        문제 1.
            Laptop 클래스의 생성자 함수를 완성해주세요.
            Laptop은 컴퓨터에 기본적으로 들어가는 부품 이외에 배터리도 추가됩니다.
            Computer 클래스에서 사용하는 변수에 battery를 추가해주세요.

            super키워드를 사용하여 상속받는 클래스에서 부모 클래스의 생성자를 사용하는 방법에 대해 익혀주세요.
            (hint)
            괄호가 빠져있지 않은지 확인해보세요~!
        """
        super().__init__(cpu, ram)
        self.battery = battery

    def battery(self):
        return('battery')



def oop_explain():
    """
    문제 2. OOP에 대해서 공부하신 내용들을 최대한 많이 작성해주세요.
    OOP의 구성에 대해서도 설명을 작성해주세요
    """

    answer = """
    
    OOP : Object Oriented Programming
    OOP의 기본전제 : 재사용이 가능하도록 설계 했는지.
    data-driven(데이터기반 의사결정), 컴퓨터하드웨어성능, 데이터양 증가에 따라 OOP활용도 증가하였다.
    머리속에서 떠올릴 수 있는것을 프로그래밍 하는것이 중요하다. (재사용 할 수 있도록 해야함)

    -구성

    캡슐화 : 내부 속성(변수)과 함수를 하나로 묶어서 클래스로 선언하는 일반적인 개념

    상속(inheritance) : "개는 동물이다." 또는 "선생님은 직장인이다."라는 관계로서 설명된다.
                        기본개념 : 상위 클래스의 모든 기능(함수, 변수)을 재사용할 수 있다.

    포함(Composition) : "개는 몸을 갖고 있다." 라는 관계로서 설명된다.
                        기본개념 : 다른 클래스의 일부 기능(함수)만을 재사용한다.        

    추상화 : 추상화는 복잡한 내용에서 핵심적인 개념 및 기능을 요악하는것을 말한다.
             기능은 없지만 선언만 해놓고 실제 기능들은 상속받은 클래스에서 동작한다.
             추상화 사용하는이유 : 클래스가 많아질것으로 예상될 때 미리 추상클래스로 틀을 잡아놓고 하위클래스의 메소드를
                                 다양하게 생성할 수 있어서 요지보수시에 좋다.

    다형성 : 같은종이지만 모습이나 고유한 특징이 다양한 성질이 있다.
            언제사용? : OOP에서 다형성은 상속받은 기능 외에 다른기능을 추가적으로 제공하고자 할 때
            장점 : 코드량 줄어든다. 가독성이 높아진다.


    
    """

    return answer