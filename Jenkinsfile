node {
    checkout scm
    docker.image('python:3.6-alpine').inside {
        stage('Build') {
            sh 'python setup.py install'
        }
        stage('Test') {
            sh 'py.test ./tests/ --verbose --junit-xml test-reports/results.xml'
        }
    }
}