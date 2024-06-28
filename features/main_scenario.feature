Feature: MainPage

    # feature 초기화 작업
    Background: 초기화
        Given Chrome 브라우저를 통해 NAVER URL에 접속한다.
        And 테스트 환경을 초기화한다.

    @main-test-1
    Scenario: 메인 페이지 접속 확인하기
        Then 네이버 검색 필드가 표시된다.

    @main-test-2
    Scenario: 프로필 영역 확인하기
        Then 프로필 영역이 표시된다.

    @main-test-3
    Scenario: 로그인 영역 UI 확인하기
        Then 로그인 안내 문구가 표시된다.
        Then 로그인 버튼이 표시된다.
        Then "아이디 찾기" 링크 텍스트가 표시된다.
        Then "비밀번호 찾기" 링크 텍스트가 표시된다.
        Then "회원가입" 링크 텍스트가 표시된다.

    @main-test-4
    Scenario: 로그인 페이지 이동하기
        When 로그인 버튼을 클릭한다.
        Then 로그인 페이지로 이동한다.

    @main-test-5
    Scenario: 네이버 카페 페이지로 이동하기
        When 네이버 카페 메뉴를 클릭한다.
        Then 네이버 카페 페이지로 이동한다.

    @main-test-6
    Scenario: 네이버 블로그 페이지로 이동하기
        When 네이버 블로그 메뉴를 클릭한다.
        Then 네이버 블로그 페이지로 이동한다.

    @main-test-7
    Scenario: 네이버 쇼핑 페이지로 이동하기
        When 네이버 쇼핑 메뉴를 클릭한다.
        Then 네이버 쇼핑 페이지로 이동한다.

    @main-test-8
    Scenario: 네이버 뉴스 페이지로 이동하기
        When 네이버 뉴스 메뉴를 클릭한다.
        Then 네이버 뉴스 페이지로 이동한다.

    @main-test-9
    Scenario: 네이버 증권 페이지로 이동하기
        When 네이버 증권 메뉴를 클릭한다.
        Then 네이버 증권 페이지로 이동한다.

    @main-test-10
    Scenario: 네이버 부동산 페이지로 이동하기
        When 네이버 부동산 메뉴를 클릭한다.
        Then 네이버 부동산 페이지로 이동한다.

    @main-test-11
    Scenario: 네이버 지도 페이지로 이동하기
        When 네이버 지도 메뉴를 클릭한다.
        Then 네이버 지도 페이지로 이동한다.

    @main-test-12
    Scenario: 네이버 웹툰 페이지로 이동하기
        When 네이버 웹툰 메뉴를 클릭한다.
        Then 네이버 웹툰 페이지로 이동한다.

    @main-test-13
    Scenario: 네이버 날씨 페이지로 이동하기
        When 네이버 날씨 링크 텍스트를 클릭한다.
        Then 네이버 날씨 페이지로 이동한다.