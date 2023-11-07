pipeline {
    agent  {label 'java11-docker-slave'}
    stages{
        stage("Compile"){
            steps{
                sh "mvn compile;"
            }
        }
        stage("Test"){
            steps{
                sh "mvn test"
            }
        }
        stage("Code coverage"){
            steps{
                publishHTML (target: [
                    reportDir: 'target/site/jacoco/com.mrcrunch91.calculator/',
                    reportFiles: 'index.html',
                    reportName: "JaCoCo Report"
                ])                
            }

    }
  }
}
