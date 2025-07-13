from abc import ABC, abstractmethod

from src.core.analyzer import CodeElement


class LLMClient(ABC):
    @abstractmethod
    def generate_docs(self, code_element: CodeElement) -> str:
        """
        Generates documentation for the given code element.
        
        Args:
            code_element (CodeElement): The code element to document.
        
        Returns:
            str: The generated documentation string.
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """
        Checks if the resource is currently available.
        
        Returns:
            bool: True if available, False otherwise.
        """
        pass
