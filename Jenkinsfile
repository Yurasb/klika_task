node {
    checkout scm
    docker.image('python:3.6-alpine').inside {
        stage('Build') {
            steps {
                sh 'python setup.py install'
            }
        }
        stage('Test') {
            steps {
                sh 'py.test ./tests/ --verbose --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}