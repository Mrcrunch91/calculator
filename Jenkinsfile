pipeline {
    
    agent any
    
    triggers {
        pollSCM('* * * * *')
    }
    
    stages{

        stage("Docker Build"){
            steps {
                sh "docker build -t mrcrunch/book-store:v1.1 ."
            }
        }
        stage ("Docker-in-Docker Run"){
            steps{
                sh 'docker run -d --rm -p 81:81 --name bookstore mrcrunch/book-store:v1.1'
            }
        }        
        stage("Acceptance Test"){
            steps{
                sh "chmod u+wrx acceptance_test.sh"
                sh "docker exec bookstore /home/jenkins/acceptance_test.sh"
            }
        }
        stage("Docker App Push"){
            steps {
                sh 'apt -yq remove golang-docker-credential-helpers'
                sh 'docker login --username mrcrunch --password LebronJames#1'
                sh 'docker push mrcrunch/book-store:v1.1'
            }
        }
    } 
    post {
        always{
            sh "docker stop bookstore"
        }
    }
}
