import os
from pathlib import Path


class Settings:
    def __init__(self) -> None:
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.output_dir = Path("docs")
        self.supported_extensions = [".py"]
        self.max_tokens = 2000
        self.temperature = 0.3


settings = Settings()
