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
        stage('Install unzip') {
            steps {
                sh '''
                # Update apt repository and install unzip
                sudo apt-get update && apt-get install -y unzip
                '''
            }
        }
        stage('Scan for XSS with Nuclei') {
            steps {
                sh '''
                # Step 1: Download and install Nuclei in this pod
                curl -s https://api.github.com/repos/projectdiscovery/nuclei/releases/latest \
                | grep "browser_download_url.*linux_amd64.zip" \
                | cut -d '"' -f 4 \
                | xargs curl -LO

                unzip nuclei*.zip
                chmod +x nuclei
                mv nuclei /usr/local/bin/

                # Step 2: Run Nuclei to scan your app
                nuclei -u https://autumncombs.github.io/capstone/ -t vulnerabilities/xss/ -o nuclei-results.txt
                '''
            }
        }
    }
}