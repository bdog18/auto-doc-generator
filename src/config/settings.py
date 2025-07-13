import os
from pathlib import Path


class Settings:
    def __init__(self) -> None:
        """
        Initializes configuration with API key, output directory, supported file extensions, token limit, and temperature.
        
        Args:
            None
        
        Returns:
            None
        """
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.output_dir = Path("docs")
        self.supported_extensions = [".py"]
        self.max_tokens = 2000
        self.temperature = 0.3


settings = Settings()
