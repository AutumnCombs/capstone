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
         stage('Scan for XSS with ZAP') {
            steps {
                echo 'Running OWASP ZAP Baseline Scan for XSS...'
                sh '''
                    docker run --rm -v $(pwd):/zap/wrk/:rw \
                    owasp/zap2docker-stable zap-baseline.py \
                    -t https://autumncombs.github.io/capstone/ \
                    -r zap_xss_report.html \
                    -I
                '''
            }
        }
    }
    post {
        always {
            echo 'Archiving ZAP XSS report...'
            archiveArtifacts artifacts: 'zap_xss_report.html', allowEmptyArchive: true
        }
    }
}