pipeline {
  agent {
    kubernetes {
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: docker
      image: docker:20.10.24-dind
      command:
        - sh
        - -c
        - |
          apk add --no-cache git curl && cat
      tty: true
      volumeMounts:
        - name: docker-sock
          mountPath: /var/run/docker.sock
        - name: workspace-volume
          mountPath: /home/jenkins/agent
    - name: zap
      image: owasp/zap2docker-weekly
      command:
        - sh
        - -c
        - |
          cat
      tty: true
      volumeMounts:
        - name: workspace-volume
          mountPath: /home/jenkins/agent
  volumes:
    - name: docker-sock
      hostPath:
        path: /var/run/docker.sock
    - name: workspace-volume
      emptyDir: {}
"""
    }
  }
  stages {
    stage('Clone the repo') {
      steps {
        container('docker') {
          echo 'clone the repo'
          sh 'rm -fr html'
          sh 'git clone https://github.com/AutumnCombs/capstone.git'
        }
      }
    }
    stage('OWASP ZAP Scan') {
      steps {
        container('zap') {
          sh '''
            zap-baseline.py \
              -t https://autumncombs.github.io/capstone/ \
              -r zap_report.html || true
          '''
          archiveArtifacts artifacts: 'zap_report.html', fingerprint: true
        }
      }
    }
    stage('Check website is up') {
      steps {
        container('docker') {
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
}