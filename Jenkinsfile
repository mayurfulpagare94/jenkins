pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/your-repo.git'
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