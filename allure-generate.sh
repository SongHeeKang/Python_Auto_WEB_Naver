# behave 테스트 수행하는 쉘스크립트 실행
./allure-behave-run.sh

# 테스트 완료 후 allure report 생성
echo "Allure 리포트 생성 중..."
allure generate reports/ -o allure-report/ --clean

# 생성된 allure report를 웹 서버를 통해 보기
echo "생성된 Allure 리포트 보기"
echo "Allure 리포트 검토 후, Ctrl + C 를 눌러 Web Server 종료"
allure serve reports

# 사용자 입력 대기 (Enter 키를 누르면 allure report가 종료되고, reports 디렉토리를 삭제함
read -p "리포트 검토 완료 후, Enter 키를 누르면 초기 상태로 복원"

# reports 디렉토리 삭제
rm -rf reports

echo "reports 디렉토리 삭제 완료 : 초기 상태로 복원"