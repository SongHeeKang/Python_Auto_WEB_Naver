pipeline {
    agent any
    // agent {
    //     docker {
    //         image 'docker:latest'
    //         args '-v /var/run/docker.sock:/var/run/docker.sock'
    //     }
    parameters {
        string(name: 'BEHAVE_FEATURE', defaultValue: 'features', description: 'Enter a value for FEATURE features/scenario.feature')
        string(name: 'PASS_SCREENSHOT', defaultValue: 'True', description: 'Enter a value for PASS_SCREENSHOT')
        string(name: 'REMOTE_RUN', defaultValue: 'REMOTE_RUN=True', description: 'Enter a value for REMOTE_RUN')
        string(name: 'SELENIUM_GRID_URL', defaultValue: 'http://127.0.0.1', description: 'Enter a value for SELENIUM_GRID_URL')
        string(name: 'SELENIUM_WAIT_TIME', defaultValue: '10', description: 'Enter a value for SELENIUM_WAIT_TIME')
    }
    environment {
        BUILD_START = "${new Date().getTime()}"
    }

    options {
        // retry(2) // 재시도 횟수
        buildDiscarder(logRotator(numToKeepStr: '100')) // 빌드 로그는 100개까지 유지
        // throttleJobProperty(
        //     categories: ['GlobalThrottle'],
        //     throttleEnabled: true,
        //     throttleOption: 'category'
        // )
    }


    stages {
        // stage('Run Selenium Grid Docker') {
        //         steps {
        //             script {
        //                 sh """
        //                 id
        //                 pwd
        //                 """
        //                 // Selenium Grid 컨테이너 실행 및 무작위 포트 설정
        //                 def container_id = sh(script: 'sudo docker run -d -P --shm-size="2g" selenium/standalone-chrome', returnStdout: true).trim()
        //                 echo "container_id = $container_id"
        //                 // 컨테이너에서 할당된 포트 확인
        //                 def allocated_port = sh(script: 'sudo docker port ' + container_id + ' 4444 | awk -F \':\' \'{print $2}\' | awk \'{print $1}\'', returnStdout: true).trim()
        //                 // 할당된 포트 출력
        //                 echo "할당된 포트: $allocated_port"
        //                 // 환경 변수로 컨테이너 ID 저장
        //                 env.CONTAINER_ID = container_id
        //                 env.CONTAINER_PORT= allocated_port

        //             }
        //         }
        //     }

        stage('Delete reports'){
            steps{
                script {
                sh """
                        rm -rf reports
                    """
                }
            }
        }

        stage('Setup Config'){
            steps{
                script {
                    def remoteRun = params.REMOTE_RUN
                    def containerPort= env.CONTAINER_PORT
                    def remoteUrl= params.SELENIUM_GRID_URL
                    def seleniumWaitTime=params.SELENIUM_WAIT_TIME

                    sh """
                        mkdir -p reports
                        sed -i 's;REMOTE_RUN=False;${remoteRun};g' config/config.py
                        sed -i 's;\\[REMOTE_URL\\];${remoteUrl}:${containerPort}/wd/hub;g' config/config.py
                        sed -i 's;\\[SELENIUM_WAIT_TIME\\];${seleniumWaitTime};g' config/config.py
                        cat config/config.py
                    """
                }
                }
        }
                

        stage('Build') {
            steps {
                script {
                    def behaveFeatureFile=params.BEHAVE_FEATURE
                    sh """
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        rm -f \$(pwd)/reports/*.xml
                        rm -f \$(pwd)/reports/*.png
                        sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' keen_moore
                        behave -f allure_behave.formatter:AllureFormatter -o \$(pwd)/reports --junit ${behaveFeatureFile} -f pretty
                    """
                    // def seleniumChromeIP = sh(script: 'sudo docker run -d -P --platform linux/amd64 --shm-size=2g selenium/standalone-chrome')
                    // echo "seleniumChromeIP = $seleniumChromeIP"
                }
            }
        }
    }
    // Allure Report 생성
    post {
        always {
            // cleanSeleniumGrid()
            publishAllureResults()
        }
    }
}



// // 함수 정의
// def cleanSeleniumGrid() {
//     sh """
//         # clean Selenium Grid Docker
//         sudo docker rm -f ${env.CONTAINER_ID}
//     """
// }


def publishAllureResults() {
    allure includeProperties: false, jdk: '', results: [[path: 'reports']]
}
