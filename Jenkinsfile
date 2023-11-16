pipeline {
    agent any
 //    {
 //      docker { 
 //           label 'Docker-Java11-Slave'
 //           image 'mrcrunch/jenkins-slave-with-java11:v1.5'                    
 //       }
 //  }
    triggers {
        pollSCM('* * * * *')
    }
    stages{
        stage("Package"){
            steps{
                sh "mvn compile package;sleep 1m"
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
        stage("Docker App Push"){
            steps {
                sh 'apt -yq remove golang-docker-credential-helpers'
                sh 'docker login --username mrcrunch --password LebronJames#1'
                sh "docker push mrcrunch/calculator:latest"
            }
        }
        stage ("Deploy to Staging"){
            steps{
                sh "docker run -d --rm -p 8765:8080 --name calculator mrcrunch/calculator:latest"
            }
        }
        stage("Acceptance Test"){
            steps{
                sleep 60
                sh "chmod +x acceptance_test.sh && sudo ./acceptance_test.sh"
            }
        }
    } 
    post {
        always{
            sh "docker stop calculator"
        }
    }
}
