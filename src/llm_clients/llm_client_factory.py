# src/utils/llm_client.py
from llm_clients.api_llm_client import OpenAIClient
from src.llm_clients.base_llm_client import LLMClient
from src.llm_clients.local_llm_client import OllamaClient


class LLMClientFactory:
    @staticmethod
    def create_client(provider: str = "auto") -> LLMClient:
        """
        Creates and returns an LLM client instance based on the specified provider.  
        Defaults to automatically selecting an available client.
        
        Args:
            provider (str): The name of the provider to use ('auto', 'ollama', 'openai').
        
        Returns:
            LLMClient: An instance of the selected LLM client.
        
        Raises:
            RuntimeError: If no available client is found when provider is 'auto'.
            ValueError: If an unknown provider is specified.
        """
        if provider == "auto":
            # Try local options first
            if OllamaClient().is_available():
                return OllamaClient()
            # elif TransformersClient().is_available():
            #     return TransformersClient()
            elif OpenAIClient().is_available():
                return OpenAIClient()  # Fallback to API
            raise RuntimeError("No available LLM client found for 'auto' provider.")

        elif provider == "ollama":
            return OllamaClient()
        # elif provider == "transformers":
        #     return TransformersClient()
        elif provider == "openai":
            return OpenAIClient()
        else:
            raise ValueError(f"Unknown provider: {provider}")
