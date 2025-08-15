#!/bin/bash

echo "Setting up Jenkins for Spring Boot CI/CD..."

# Wait for Jenkins to be ready
echo "Waiting for Jenkins to start..."
sleep 30

# Get Jenkins CLI jar
wget http://localhost:8080/jnlpJars/jenkins-cli.jar

# Install required plugins
echo "Installing Jenkins plugins..."
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin workflow-aggregator
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin git
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin maven-plugin
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin junit
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin htmlpublisher
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin ws-cleanup
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin dependency-check-jenkins-plugin

# Restart Jenkins to apply plugins
echo "Restarting Jenkins to apply plugins..."
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart

echo "Jenkins setup complete!"
echo "Access Jenkins at: http://localhost:8080"
echo "Default credentials: admin/admin" 