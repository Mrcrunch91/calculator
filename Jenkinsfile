pipeline {
    agent  { label 'java11-docker-slave'}
    triggers {
        pollSCM('* * * * *')
    }
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
        stage("Code Coverage"){
            steps{
                publishHTML (target: [
                    reportDir: 'target/site/jacoco/com.mrcrunch91.calculator/',
                    reportFiles: 'index.html',
                    reportName: "JaCoCo Report"
                ])                
            }

        }
        stage("Static Code Analysis"){
            steps{
                sh "mvn validate"
                publishHTML (target: [
                    reportDir: 'target/site/jacoco/com.mrcrunch91.calculator/',
                    reportFiles: 'main.html',
                    reportName: "Checkstyle Report"
                ])
            }
        }
    }
}
