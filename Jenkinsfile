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
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'set "PATH=C:\\Users\\HP\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%" && docker build -t student-result-devops .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'set "PATH=C:\\Users\\HP\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%" && docker rm -f student-result-devops-container || exit 0'
                bat 'set "PATH=C:\\Users\\HP\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%" && docker run -d --name student-result-devops-container -p 5001:5000 student-result-devops'
            }
        }

    }
}