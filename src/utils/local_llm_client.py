# src/utils/local_llm_client.py
import requests

from src.utils.llm_client import LLMClient


class OllamaClient(LLMClient):
    def __init__(self, model: str = "deepseek-coder") -> None:
        self.model = model
        self.base_url = "http://localhost:11434"

    def is_available(self) -> bool:
        # Implement logic to check if Ollama is available
        return True  # Placeholder for actual availability check

    def generate_docs(self, code_element: str) -> str:
        prompt = f"""Generate documentation for this function:

                    {code_element}

                    Provide:
                    1. Brief description
                    2. Parameters
                    3. Returns
                    4. Example usage"""

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False},
        )

        return str(response.json()["response"])


if __name__ == "__main__":
    # Example usage
    elem = "def add(a, b): return a + b"
    client = OllamaClient()
    response = client.generate_docs(code_element=elem)  # Example usage
    print(response)
