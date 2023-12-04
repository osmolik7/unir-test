pipeline {
    agent any
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/osmolik7/unir-test.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Run App') {
            steps {
                echo 'Corriendo la aplicacion!'
                sh 'make run'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('API tests') {
            steps {
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('E2E tests') {
            steps {
                //sh 'make test-e2e'
                //archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('mail') {
            steps {
                echo 'Enviando correo ...'
                mail subject: "${env.JOB_NAME} - Build #${env.BUILD_NUMBER} Status",
                    body: "El trabajo ${env.JOB_NAME} - Build #${env.BUILD_NUMBER} ha terminado.",
                    to: 'camacho044@gmail.com',
                    from: 'jenkins@localhost.com'
            }
        }
    }
    post {
        failure {
            mail subject: "${env.JOB_NAME} - Build #${env.BUILD_NUMBER} FAILED",
                body: "El trabajo ${env.JOB_NAME} - Build #${env.BUILD_NUMBER} ha fallado.",
                to: 'camacho044@gmail.com',
                from: 'jenkins@localhost.com'
        }
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
    }
}
