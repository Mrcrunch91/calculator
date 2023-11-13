FROM mrcrunch/jenkins-slave-with-java11:v1.3
COPY target/calculator-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java", "-jar","app.jar"]