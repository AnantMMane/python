# AI-Driven QA Test Generation and Automation

This project leverages AI/ML to auto-generate robust backend tests and identify risky logic paths, with a primary focus on Java Spring-based microservices.

---

## Sample Spring Boot Microservice: `spring-boot-sample-app`

### Features
- REST API with GET, POST, and PUT endpoints
- Auto-generated OpenAPI/Swagger documentation
- Common microservices dependencies (Actuator, Validation, Lombok, H2, Testcontainers)

### Directory Structure
- `/spring-boot-sample-app` - Main Spring Boot microservice
- `/shared` - Common Java libraries/utilities
- `/contracts` - OpenAPI specs, Pact files
- `/ml` - ML models/scripts
- `/scripts` - Automation scripts
- `/reports` - Test/coverage reports
- `/ci-pipelines` - CI/CD configs
- `/docs` - Documentation
- `/test-data` - Sample/generated data

---

## Setup Instructions

### Prerequisites
- Java 17+
- Maven 3.8+

### Build the Application
```sh
cd spring-boot-sample-app
./mvnw clean install
```

### Run the Application
```sh
./mvnw spring-boot:run
```
The app will start on [http://localhost:8080](http://localhost:8080)

### API Documentation (Swagger UI)
- Visit: [http://localhost:8080/swagger-ui.html](http://localhost:8080/swagger-ui.html)
- Or: [http://localhost:8080/swagger-ui/index.html](http://localhost:8080/swagger-ui/index.html)

---

## API Endpoints

### 1. `GET /hello`
Returns a greeting message.

**Sample cURL:**
```sh
curl -X GET http://localhost:8080/hello
```
**Sample Response:**
```json
{"message": "Hello from Spring Boot!"}
```

---

### 2. `POST /hello`
Accepts a JSON payload and echoes it back with a confirmation message.

**Sample cURL:**
```sh
curl -X POST http://localhost:8080/hello \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "age": 30}'
```
**Sample Response:**
```json
{
  "message": "POST received!",
  "received": {
    "name": "Alice",
    "age": 30
  }
}
```

---

### 3. `PUT /hello/{id}`
Accepts an ID as a path variable and a JSON payload, returns a confirmation message with the updated data.

**Sample cURL:**
```sh
curl -X PUT http://localhost:8080/hello/123 \
  -H "Content-Type: application/json" \
  -d '{"status": "active"}'
```
**Sample Response:**
```json
{
  "message": "PUT received!",
  "id": "123",
  "updated": {
    "status": "active"
  }
}
```

---

## Automated Test Generation with Ollama (Local LLM)

This project supports automated unit and integration test generation for Java classes using a local LLM (e.g., CodeLlama via Ollama) and a Python script.

### Python Environment Setup

1. **Create and activate a virtual environment:**
   - Windows:
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Install required packages:**
   ```sh
   pip install -r scripts/requirements.txt
   ```

### Running the Test Generation Script

- Make sure your Ollama server is running with a code-capable model (e.g., `codellama:7b`).
- Run the script:
  ```sh
  python scripts/generate_tests_with_ollama.py
  ```
- This will generate unit and integration tests for all Java classes under `src/main/java` and place them in the corresponding `src/test/java` package structure.

---

### Manual Test Case Generation

Test cases are generated using an external Python script. This is now the recommended and only supported way to generate tests.

#### Steps

1. **Ensure Ollama is running** with a code-capable model (e.g., `codellama:7b`).
2. **Activate your Python environment** (if not already active):
   - Windows:
     ```sh
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
3. **Run the test generation script for the Spring Boot app:**
   ```sh
   python scripts/generate_tests_with_ollama.py --source-dir spring-boot-sample-app/src/main/java/com/example/demo --test-dir spring-boot-sample-app/src/test/java/com/example/demo
   ```
   - This will generate or update test files for all modules in `spring-boot-sample-app`.

**Note:**  
You can adjust the `--source-dir` and `--test-dir` arguments to target other modules or packages as needed.

---

## CI/CD Workflow Documentation

### Overview
This project uses a Jenkins-based CI/CD pipeline to ensure code quality, contract compliance, and security for all Spring Boot microservices. The pipeline is designed for continuous integration and contract-first development.

### Pipeline Stages
1. **Checkout**: Pulls the latest code from the repository.
2. **Build**: Compiles the project using Maven.
3. **Test**: Runs all unit and integration tests. Publishes JUnit and JaCoCo code coverage reports.
4. **Contract Verification**: Runs contract tests generated from Groovy/YAML contracts using Spring Cloud Contract. Ensures all API endpoints are compliant with their contracts. Fails the build if any contract is broken.
5. **Security Scan**: Uses OWASP Dependency Check to scan for known vulnerabilities in dependencies. Fails the build if any high-severity vulnerabilities are found.
6. **Package**: Packages the application as a JAR and archives it as a build artifact.

### Key Features
- **Contract-First Development**: API contracts are defined in `src/test/resources/contracts` using Groovy or YAML. Spring Cloud Contract generates and runs tests to enforce these contracts.
- **Security Compliance**: The pipeline enforces a strict security gate using OWASP Dependency Check. Vulnerable dependencies must be updated before merging.
- **Automated Reporting**: Test and code coverage reports are published as HTML artifacts for each build.
- **Continuous Verification**: The pipeline runs automatically on every commit (via SCM polling or webhook) to catch issues early.

### How to Add/Update Contracts
1. Add a new Groovy or YAML contract file to `src/test/resources/contracts` for each new or updated endpoint.
2. The next pipeline run will auto-generate and execute tests for the new contract.
3. If the implementation does not match the contract, the build will fail.

### How to Run Locally
1. Run all tests and contract verification:
   ```sh
   ./mvnw clean verify
   ```
2. View test and coverage reports in `target/site/` and `target/site/jacoco/`.

### Troubleshooting
- **Contract Test Failures**: Check the generated test sources in `target/generated-test-sources/contracts` and the contract files for mismatches.
- **Security Scan Failures**: Update dependencies in `pom.xml` to resolve vulnerabilities.
- **Missing Reports**: Ensure all report directories exist or remove their publishing blocks from the Jenkinsfile.

### Best Practices
- Always update or add contracts when changing API endpoints.
- Keep dependencies up to date to avoid security issues.
- Use the pipeline as the source of truth for build and test status.

---

## Notes
- The app uses in-memory H2 database for development/testing.
- All endpoints and models are auto-documented via Swagger/OpenAPI.
- For more endpoints and features, see the source code in `/spring-boot-sample-app/src/main/java/com/example/demo/controller/`. 