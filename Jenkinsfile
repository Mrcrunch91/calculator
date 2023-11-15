pipeline {
    agent  {
        docker { 
            label 'Docker-Java11-Slave'
            image 'mrcrunch/jenkins-slave-with-java11:v1.3'
            args '-v /var/run/docker.sock:/var/run/docker.sock'        
        }
    }
    triggers {
        pollSCM('* * * * *')
    }
    stages{
        stage("Package"){
            steps{
                sh "mvn compile package;"
            }
        }
        stage("Docker Build"){
            steps {
                sh "docker build -t mrcrunch/calculator ."
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
