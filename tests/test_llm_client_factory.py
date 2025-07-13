from unittest.mock import patch

import pytest

from src.llm_clients.base_llm_client import LLMClient
from src.llm_clients.llm_client_factory import LLMClientFactory


class TestLLMClientFactory:
    def test_create_openai_client(self):
        """Test creating OpenAI client."""
        client = LLMClientFactory.create_client("openai")
        assert client is not None
        assert isinstance(client, LLMClient)

    def test_create_ollama_client(self):
        """Test creating Ollama client."""
        client = LLMClientFactory.create_client("ollama")
        assert client is not None
        assert isinstance(client, LLMClient)

    def test_unknown_provider_raises_error(self):
        """Test that unknown provider raises ValueError."""
        with pytest.raises(ValueError, match="Unknown provider"):
            LLMClientFactory.create_client("unknown_provider")

    @patch("src.llm_clients.local_llm_client.OllamaClient.is_available")
    def test_auto_selects_ollama_when_available(self, mock_is_available):
        """Test auto selection prefers Ollama when available."""
        mock_is_available.return_value = True

        client = LLMClientFactory.create_client("auto")
        assert client.__class__.__name__ == "OllamaClient"

    @patch("src.llm_clients.local_llm_client.OllamaClient.is_available")
    @patch("src.llm_clients.api_llm_client.OpenAIClient.is_available")
    def test_auto_fallback_to_openai(
        self, mock_openai_available, mock_ollama_available
    ):
        """Test auto selection falls back to OpenAI when Ollama unavailable."""
        mock_ollama_available.return_value = False
        mock_openai_available.return_value = True

        client = LLMClientFactory.create_client("auto")
        assert client.__class__.__name__ == "OpenAIClient"
