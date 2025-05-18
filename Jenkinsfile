pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: '/workspaces/jenkins/main.py'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running unit tests..."'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying to production..."'
            }
        }
    }
}