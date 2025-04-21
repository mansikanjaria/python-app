pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build/Run') {
            steps {
                sh 'python app.py'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('MySonarQube') {
                    sh 'sonar-scanner -Dsonar.projectKey=simple-python-app -Dsonar.sources=. -Dsonar.host.url=http://52.228.189.60:9000 -Dsonar.login=squ_d172193ac04d45d2f67c6319e29c6d35e847dacb'
                }
            }
        }

        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }

    triggers {
        cron('H 10 * * *')
    }
}
