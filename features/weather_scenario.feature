Feature: WeatherPage

    # feature 초기화 작업
    Background: 초기화
        Given Chrome 브라우저를 통해 NAVER URL에 접속한다.
        And 테스트 환경을 초기화한다.

    @weather-test-1
    Scenario: 날씨 페이지 홈 탭 확인하기
        When 네이버 날씨 링크 텍스트를 클릭한다.
        Then 네이버 날씨 페이지로 이동한다.
        Then 네이버 날씨 홈 탭이 표시된다.

    @weather-test-2
    Scenario: 날씨 페이지 예보비교 탭 확인하기
        When 네이버 날씨 링크 텍스트를 클릭한다.
        Then 네이버 날씨 페이지로 이동한다.
        Then 네이버 날씨 예보비교 탭이 표시된다.

    @weather-test-3
    Scenario: 날씨 페이지 지도 탭 확인하기
        When 네이버 날씨 링크 텍스트를 클릭한다.
        Then 네이버 날씨 페이지로 이동한다.
        Then 네이버 날씨 미세먼지 탭이 표시된다.

    @weather-test-4
    Scenario: 날씨 페이지 영상 탭 확인하기
        When 네이버 날씨 링크 텍스트를 클릭한다.
        Then 네이버 날씨 페이지로 이동한다.
        Then 네이버 날씨 지도 탭이 표시된다.