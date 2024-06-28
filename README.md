# Repository 소개
- behave를 사용한 자동화 스크립트를 관리하는 레포지토리 입니다.

# Use Tool
- **Language**
  - Python
  - Gherkin
  - Shell
- **Framework**
  - Selenium
- **BDD**
  - behave
- **Report**
  - Allure
- **Design Pattern**
  - Page Object Model

# 환경 셋업
- **selenium 을 설치한다.**
  - window os : ```pip install selenium```
  - mac os : ```pip3 install selenium```
- **behave 를 설치한다.**
  - window os : ```pip install behave```
  - mac os : ```pip3 install behave```
- **allure commandline 을 설치한다.**
  - window : ```scoop install allure```
  - mac os : ```brew install allure```
- **allure 를 설치한다.**
  - window : ```pip install allure-behave```
  - mac os : ```pip3 intall allure-behave```
    
# 실행 구조 및 방법 (behave 프레임워크만 실행하기)
- 커맨드라인에서 **아래 명령어**를 통해 실행할 수 있습니다.
  - ```behave features/{추가 하위 디렉토리.feature}```
  - 추가 하위 디렉토리를 입력하면 해당 feature 파일만 실행하고, beahve features/ 를 입력하면 모든 feature 파일을 실행하는 구조
- behave 시나리오는 steps/Steps.py 파일에 있는 함수를 순차적으로 실행합니다. 또한 feature 파일 내에 있는 given, when, then 시나리오를 순차적으로 실행하고, 구현되지 않은 시나리오는 NotImplmentedError 를 발생시킵니다.

# 실행 구조 및 방법 (behave 수행 후 allure 리포트 생성하기)
- 커맨드라인에서 **아래 명령어**를 통해 실행할 수 있습니다.
  - ```./allure-generate.sh```
  - behave 를 통해 **테스트 결과 데이터를 누적**하고, 이를 기반으로 **테스트 리포트를 생성**합니다.
