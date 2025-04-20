pipeline {
  agent {
    kubernetes {
      yaml """
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: zap
            image: owasp/zap2docker-stable
            command:
            - cat
            tty: true
      """
    }
  }
  stages {
    stage('ZAP Scan') {
      steps {
        container('zap') {
          sh '''
            zap-baseline.py -t https://6445-204-8-53-10.ngrok-free.app -r zap_report.html
          '''
        }
      }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: 'zap_report.html', allowEmptyArchive: true
    }
  }
}