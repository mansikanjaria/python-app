pipeline {
    agent any

    environment {
        GIT_REPO = "https://github.com/mansikanjaria/python-app.git"
    }

    stages {
        stage('Manual Git Checkout') {
            steps {
                sh 'rm -rf python-app || true'
                sh 'git clone $GIT_REPO'
                sh 'ls -la python-app'
            }
        }

        stage('Run Python') {
            steps {
                sh 'cd python-app && python3 app.py'
            }
        }
    }
}
