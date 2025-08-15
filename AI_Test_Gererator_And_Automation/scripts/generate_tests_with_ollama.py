import os
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "codellama:7b"


def generate_test(java_code, prompt_type="unit"):
    if prompt_type == "unit":
        prompt = (
            "Write a JUnit 5 unit test class for the following Spring Boot Java class. "
            "Use Mockito for dependencies. Cover all public methods. "
            "Only output valid Java code, no explanations or markdown.\n"
            f"{java_code}"
        )
    else:
        prompt = (
            "Write a JUnit 5 integration test class for the following Spring Boot Java class. "
            "Use @SpringBootTest and MockMvc if it's a controller. "
            "Only output valid Java code, no explanations or markdown.\n"
            f"{java_code}"
        )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def process_file(src_path, src_root, test_root, prompt_type="unit"):
    # Compute relative path from src_root
    rel_path = os.path.relpath(src_path, src_root)
    # Change src/main/java to src/test/java and add Ollama[Type]Test to filename
    test_dir = os.path.join(test_root, os.path.dirname(rel_path))
    os.makedirs(test_dir, exist_ok=True)
    class_name = os.path.splitext(os.path.basename(src_path))[0]
    test_file = os.path.join(test_dir, f"{class_name}Ollama{prompt_type.capitalize()}Test.java")
    with open(src_path, "r") as f:
        java_code = f.read()
    test_code = generate_test(java_code, prompt_type)
    with open(test_file, "w") as f:
        f.write(test_code)
    print(f"Generated test: {test_file}")


def find_java_files(root):
    java_files = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".java"):
                java_files.append(os.path.join(dirpath, filename))
    return java_files


if __name__ == "__main__":
    src_root = "spring-boot-sample-app/src/main/java"
    test_root = "spring-boot-sample-app/src/test/java"
    java_files = find_java_files(src_root)

    for src_path in java_files:
        # Generate unit test
        process_file(src_path, src_root, test_root, prompt_type="unit")
        # Generate integration test
        process_file(src_path, src_root, test_root, prompt_type="integration") 