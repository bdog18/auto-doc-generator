from abc import ABC, abstractmethod

from src.core.analyzer import CodeElement


class LLMClient(ABC):
    @abstractmethod
    def generate_docs(self, code_element: CodeElement) -> str:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass
