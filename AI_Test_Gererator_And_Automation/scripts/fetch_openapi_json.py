import requests
import os

OPENAPI_URL = "http://localhost:8080/v3/api-docs"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "contracts", "openapi.json")

if __name__ == "__main__":
    response = requests.get(OPENAPI_URL)
    response.raise_for_status()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"OpenAPI JSON saved to {OUTPUT_PATH}") 