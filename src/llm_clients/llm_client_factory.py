# src/utils/llm_client.py
from llm_clients.api_llm_client import OpenAIClient
from src.llm_clients.base_llm_client import LLMClient
from src.llm_clients.local_llm_client import OllamaClient


class LLMClientFactory:
    @staticmethod
    def create_client(provider: str = "auto") -> LLMClient:
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
