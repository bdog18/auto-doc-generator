# src/utils/llm_client.py
from abc import ABC, abstractmethod

from src.utils.local_llm_client import OllamaClient


class LLMClient(ABC):
    @abstractmethod
    def generate_docs(self, code_element) -> str:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass


class LLMClientFactory:
    @staticmethod
    def create_client(provider: str = "auto") -> LLMClient:
        if provider == "auto":
            # Try local options first
            if OllamaClient().is_available():
                return OllamaClient()
            # elif TransformersClient().is_available():
            #     return TransformersClient()
            # else:
            #     return OpenAIClient()  # Fallback to API
            raise RuntimeError("No available LLM client found for 'auto' provider.")

        elif provider == "ollama":
            return OllamaClient()
        # elif provider == "transformers":
        #     return TransformersClient()
        # elif provider == "openai":
        #     return OpenAIClient()
        else:
            raise ValueError(f"Unknown provider: {provider}")
