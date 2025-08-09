# src/utils/local_llm_client.py
import requests

from src.core.analyzer import CodeElement
from src.llm_clients.base_llm_client import LLMClient


class OllamaClient(LLMClient):
    def __init__(self, model: str = "deepseek-coder-v2:16b") -> None:
        """
        Initializes a new instance of the class with a default model and base URL.
        
        Args:
            self: The instance being initialized.
            model (str): The name of the model to be used, defaults to "deepseek-coder-v2:16b".
            base_url (str): The base URL for API requests, defaults to "http://localhost:11434".
        
        Returns:
            None
        """
        self.model = model
        self.base_url = "http://localhost:11434"

    def is_available(self) -> bool:
        """
        Checks if Ollama is available by implementing a logic to verify its status.
        
        Returns:
            bool: True if Ollama is available, False otherwise.
        """
        # Implement logic to check if Ollama is available
        return True  # Placeholder for actual availability check

    def generate_docs(self, code_element: CodeElement) -> str:
        """
        Generates a clean Python docstring for the given function using Google-style format.
        
        Args:
            self: The instance of the class containing the function.
            code_element (CodeElement): An object representing the code element to generate the docstring for.
        
        Returns:
            str: A formatted string containing the generated docstring.
        """
        prompt = f"""
            Generate ONLY a clean Python docstring for this function. 
            Return the docstring content with triple quotes.

            Function code:
            {code_element.source_code}

            Requirements:
            - Maximum 2 sentences for description
            - Use Google-style format
            - Be extremely concise
            - Only include sections that are relevant
            - No explanatory text outside the docstring
            - Always return docstring with triple quotes before and after
            - Make sure to return all sections from the example output format
            - Make sure to include an example if possible

            Example output format:
            /"/"/"
            Brief one-sentence description of what the function does.

            Args:
                param_name (type): Brief description.

            Returns:
                type: Brief description.

            Example:
                >>> function_name(args)
                expected_result

            Generate docstring now:
            /"/"/"
            """

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False},
        )
        return str(response.json()["response"].strip())


if __name__ == "__main__":
    # Example usage
    elem = CodeElement(
        name="test_func", type="def", source_code="def add(a, b): return a + b"
    )
    client = OllamaClient()
    response = client.generate_docs(code_element=elem)  # Example usage
    print(response)

