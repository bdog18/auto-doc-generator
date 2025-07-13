# src/utils/local_llm_client.py
import requests

from src.core.analyzer import CodeElement
from src.llm_clients.base_llm_client import LLMClient


class OllamaClient(LLMClient):
    def __init__(self, model: str = "deepseek-coder") -> None:
        """
        Initializes the instance with a specified model and base URL.
        
        Args:
            model (str): The model name to use.
        
        Returns:
            None: This constructor does not return a value.
        """
        self.model = model
        self.base_url = "http://localhost:11434"

    def is_available(self) -> bool:
        """
        Checks if Ollama is available.
        
        Returns:
            bool: True if Ollama is available, False otherwise.
        """
        # Implement logic to check if Ollama is available
        return True  # Placeholder for actual availability check

    def generate_docs(self, code_element: CodeElement) -> str:
        """
        Generates a clean Python docstring for the given function code element. 
        
        Args:
            code_element (CodeElement): The code element containing the source code to document.
        
        Returns:
            str: The generated docstring in Google style format.
        
        Example:
            >>> generate_docs(code_element)
            '"""Brief description.\n\nArgs:\n    code_element (CodeElement): The code element containing the source code.\n\nReturns:\n    str: The generated docstring."""'
        """
        prompt = f"""
            Generate ONLY a clean Python docstring for this function. 
            Return the docstring content without triple quotes.

            Function code:
            {code_element.source_code}

            Requirements:
            - Maximum 2 sentences for description
            - Use Google-style format
            - Be extremely concise
            - Only include sections that are relevant
            - No explanatory text outside the docstring
            - No code examples in markdown blocks

            Example output format:
            Brief one-sentence description of what the function does.

            Args:
                param_name (type): Brief description.

            Returns:
                type: Brief description.

            Example:
                >>> function_name(args)
                expected_result

            Generate docstring now:
            """

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False},
        )

        return str(response.json()["response"])


if __name__ == "__main__":
    # Example usage
    elem = CodeElement(
        name="test_func", type="def", source_code="def add(a, b): return a + b"
    )
    client = OllamaClient()
    response = client.generate_docs(code_element=elem)  # Example usage
    print(response)
