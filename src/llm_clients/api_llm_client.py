# src/utils/local_llm_client.py
from openai import OpenAI

from src.config.settings import settings
from src.core.analyzer import CodeElement
from src.llm_clients.base_llm_client import LLMClient


class OpenAIClient(LLMClient):
    def __init__(self) -> None:
        self.client = OpenAI()
        self.client.api_key = str(settings.openai_api_key)

    def is_available(self) -> bool:
        # Implement logic to check if OpenAI is available
        return True  # Placeholder for actual availability check

    def generate_docs(self, code_element: CodeElement) -> str:
        prompt = f"""
            Generate ONLY a clean Python docstring for this function. 
            Return the docstring content without triple quotes.

            Function: {code_element.name}
            Code: {code_element.source_code}

            Requirements:
            - Maximum 2 sentences for description
            - Use Google-style format
            - Be extremely concise
            - Only include sections that are relevant
            - No explanatory text outside the docstring
            - No code examples in markdown blocks
            - Make sure to return all sections from the example output format

            Example output format:
            /"/"/"
            Brief  description of what the function does.

            Args:
                param_name (type): Brief description.

            Returns:
                type: Brief description.

            Example:
                >>> function_name(args)
                expected_result
            /"/"/"
                
            Generate docstring now:
            """

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=settings.max_tokens,
            temperature=settings.temperature,
        )

        return str(response.choices[0].message.content)


if __name__ == "__main__":
    # Example usage
    elem = CodeElement(
        name="test_func",
        type="def",
        source_code="def add(a: int, b: int) -> int: return a + b",
    )
    client = OpenAIClient()
    response = client.generate_docs(code_element=elem)  # Example usage
    print(response)
