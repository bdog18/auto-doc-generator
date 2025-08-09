import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    def __init__(self) -> None:
        """Initializes the class with environment variables for OpenAI API key, output directory, supported file extensions, and token limits and temperature settings."""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.output_dir = Path("docs")
        self.supported_extensions = [".py"]
        self.max_tokens = int(os.getenv("MAX_TOKENS", 2000))
        self.temperature = float(os.getenv("TEMPERATURE", 0.3))


settings = Settings()
