pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                    sh 'git config remote.origin.url https://github.com/mansikanjaria/python-app.git'
                }
            }
        }
    }
}
