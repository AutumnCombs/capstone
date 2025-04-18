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
        stage('Test - HTML Lint') {
            steps {
                echo 'Running HTMLhint for linting'
                sh 'htmlhint ./'
            }
        }
        stage('Test - Secrets Scan') {
            steps {
                echo 'Running trufflehog for secrets scanning'
                sh 'pip install --quiet trufflehog'
                sh 'trufflehog filesystem . || echo "Possible secrets found!"'
            }
        }
        stage('Check website is up') {
            steps {
                echo 'Check website is up'
                sh '''
                    STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://autumncombs.github.io/capstone/)
                    if [ "$STATUS" -eq 200 ]; then
                        echo "Website is UP (Status: $STATUS)"
                    else
                        echo "Website might be DOWN (Status: $STATUS)"
                    exit 1
                    fi
                '''
            }
        }
    }
}