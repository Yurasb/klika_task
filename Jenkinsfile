node {
    checkout scm
    docker.image('joyzoursky/python-chromedriver:3.6-xvfb').inside {
        stage('Build') {
            sh 'python setup.py install'
        }
        stage('Test') {
            sh 'py.test ./tests/ --verbose --junit-xml test-reports/results.xml'
        }
    }
}