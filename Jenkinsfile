pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build and Push Docker Images') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }
        stage('Deploy to Render') {
            steps {
                script {
                    sh './deploy-to-render.sh'
                }
            }
        }
    }
}
