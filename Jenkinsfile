pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Python App') {
            steps {
                sh 'echo "print(\\"Hello from Jenkins!\\")" > app.py'
                sh 'python3 app.py'
            }
        }

        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }
}
