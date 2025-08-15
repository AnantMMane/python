# Jenkins CI/CD Setup for AI Test Generator Project

This directory contains the Jenkins CI/CD configuration for the Spring Boot microservice.

## Prerequisites

You already have Jenkins running locally via Docker. This setup provides the pipeline configuration to use with your existing Jenkins instance.

## Using Your Existing Jenkins

### 1. Access Your Jenkins
- **URL:** http://localhost:8080 (or your configured port)
- Use your existing Jenkins credentials

### 2. Required Jenkins Plugins
Ensure your Jenkins has these plugins installed:
- **Pipeline** (workflow-aggregator)
- **Git**
- **Maven Integration**
- **JUnit**
- **HTML Publisher**
- **Workspace Cleanup**
- **OWASP Dependency Check** (optional, for security scanning)

### 3. Configure Tools in Jenkins
In Jenkins → **Manage Jenkins** → **Global Tool Configuration**:
- **JDK:** Configure JDK 17
- **Maven:** Configure Maven 3.9.6

## Creating the Jenkins Job

1. **New Item** → **Pipeline**
2. **Pipeline script from SCM** → **Git**
3. **Repository URL:** Your Git repository URL
4. **Script Path:** `ci-pipelines/Jenkinsfile`
5. **Save** and **Build Now**

## Jenkins Pipeline Features

### Stages:
1. **Checkout** - Clone the repository
2. **Build** - Compile the Spring Boot application
3. **Test** - Run unit and integration tests
4. **Security Scan** - OWASP dependency check
5. **Package** - Create JAR artifact

### Reports:
- **Test Results** - JUnit test reports
- **Security Report** - OWASP vulnerability scan
- **Artifacts** - Built JAR files

## Optional: Separate Jenkins Instance

If you prefer a separate Jenkins instance for this project:

```bash
cd ci-pipelines
docker-compose --profile optional up -d
```

This will start Jenkins on port **8081** to avoid conflicts with your existing instance.

## Troubleshooting

### Pipeline fails:
- Verify Maven and JDK tools are configured in Jenkins
- Check the Jenkinsfile syntax
- Review build logs for specific errors
- Ensure all required plugins are installed

### Missing plugins:
- Go to **Manage Jenkins** → **Manage Plugins**
- Install any missing plugins listed above

## Next Steps

After the pipeline is running:
1. Monitor build results
2. Review test and security reports
3. Proceed to automated test generation
4. Set up ML-based test prioritization

## Integration with AI/ML

This Jenkins setup provides the foundation for:
- Automated test generation (EvoSuite, Diffblue)
- ML-based test prioritization
- Test coverage analytics
- Security vulnerability tracking 