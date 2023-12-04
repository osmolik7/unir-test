pipeline {
    agent any
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/jeffersonricardherrera063/jenkins.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('mail') {
            steps {
                echo 'Enviando correo ...'
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
    }
}
