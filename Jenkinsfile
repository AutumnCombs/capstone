pipeline {
    agent any 
    stages {
        stage('Clone the repo') {
            steps {
                echo 'clone the repo'
                sh 'rm -fr html'
                sh 'git clone https://github.com/AutumnCombs/capstone.git'
            }
        }
        stage('push repo to remote host') {
            steps {
                echo 'connect to remote host and pull down the latest version'
            }
        }
        stage('Check website is up') {
            steps {
                echo 'Check website is up'
            }
        }
    }
}