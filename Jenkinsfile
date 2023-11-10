pipeline {
    agent  { label 'java11-docker-slave'}
    triggers {
        pollSCM('* * * * *')
    }
    stages{
        stage("Test"){
            steps{
                sh "python3 unittest"
            }
        }
    }
}
