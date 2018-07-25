pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.6-alpine'
                }
            }
            steps {
                sh 'python setup.py install'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test ./tests/ --junitxml=./test_report.xml --alluredir=./test_report/'
            }
            post {
                always {
                    junit './test_report.xml'
                    allure './test_report/'
                }
            }
        }
    }
}