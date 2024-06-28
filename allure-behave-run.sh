# behave를 이용해 자동화 테스트를 수행하고, reports 디렉토리를 생성 후 테스트 기록을 하위에 저장
echo "Behave 자동화 테스트 수행 중..."
behave -f allure_behave.formatter:AllureFormatter -o reports/ features