Feature: LoginPage

    # feature 초기화 작업
    Background: 초기화
        Given Chrome 브라우저를 통해 NAVER URL에 접속한다.
        And 테스트 환경을 초기화한다.

    @login-test-1
    Scenario Outline: 유효하지 않은 계정으로 로그인 시도하기
        When 로그인 버튼을 클릭한다.
        And "<id>" 및 "<password>" 입력한다.
        And 로그인 페이지에서 로그인 버튼을 클릭한다.
        Then 로그인에 실패하고 "<error_message>" 표시된다.
        Examples:
            | id | password | error_message |
            | <empty> | <empty> | 아이디를 입력해 주세요. |
            # | <empty> | "보안 상 비밀번호 제거" | 아이디를 입력해 주세요. |
            # | "보안 상 아이디 제거" | <empty> | 비밀번호를 입력해 주세요. |
            | invalid_id | aW52YWxpZF9wdw== | 아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다. 입력하신 내용을 다시 확인해주세요.|