node {
    checkout scm
    docker.image('joyzoursky/python-chromedriver:3.6-xvfb').inside {
        stage('Build') {
            sh 'python setup.py install'
        }
        try {
            stage('Test') {
                sh 'py.test ./tests/ --verbose --junit-xml test-reports/results.xml'
            }
        } finally {
            junit 'test-reports/results.xml'
        }
    }
}