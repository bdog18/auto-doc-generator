from abc import ABC, abstractmethod

from src.core.analyzer import CodeElement


class LLMClient(ABC):
    @abstractmethod
    def generate_docs(self, code_element: CodeElement) -> str:
        """
        Generates a documentation string for the given code element.
        
        Args:
            self (object): The instance of the class containing the method.
            code_element (CodeElement): The code element to generate documentation for.
        
        Returns:
            str: A generated documentation string in a specified format.
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """
        Determines if the service is available.
        
        Returns:
            bool: True if the service is available, False otherwise.
        """
        pass
