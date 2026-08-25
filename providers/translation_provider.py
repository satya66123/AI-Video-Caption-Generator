"""Translation provider interface."""

from abc import ABC, abstractmethod


class TranslationProvider(ABC):
    """Base interface for caption translation providers."""

    @abstractmethod
    def translate(
        self,
        text: str,
        target_language: str,
    ) -> str:
        """Translate text into the target language."""
        raise NotImplementedError
