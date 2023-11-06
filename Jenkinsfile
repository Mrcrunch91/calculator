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
    }
}
