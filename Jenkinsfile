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
        stage('OWASP ZAP Scan') {
            steps {
                sh '''
                docker run -t owasp/zap2docker-stable zap-baseline.py -t http://your-app-url -r zap_report.html || true
                '''
                archiveArtifacts artifacts: 'zap_report.html', fingerprint: true
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