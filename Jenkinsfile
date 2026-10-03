pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-result-devops .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f student-result-devops-container || exit 0'
                bat 'docker run -d --name student-result-devops-container -p 5000:5000 student-result-devops'
            }
        }
    }
}
