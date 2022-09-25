from abc import ABC, abstractstaticmethod
import re


class AbstractFilter(ABC):
    """Abstract filter.
    
    You can inherit it to create your own logic.
    """
    @staticmethod
    def _load_from_file(path: str, encoding: str="utf-8") -> None:
        """Load words from file."""
        with open(path, "r", encoding=encoding) as words:
            return [word if word[-1] != "\n" else word[:-1] for word in words]

    @abstractstaticmethod
    def is_clean(text: str) -> bool:
        """Check if sentence contains swear words."""
        pass 
    
    @abstractstaticmethod
    def censor(text: str, character: str="*") -> str:
        """Censor swear words in sentence."""
        pass 


class FilterProvider:
    """Provider for censor filters."""
    _filters: list[AbstractFilter] = []

    def register_filters(self, *filters: type[AbstractFilter]) -> None:
        """Register filters."""
        for filter in filters:
            self._filters.append(filter)

    def censore(self, text: str, character: str="*") -> str:
        """Censore text by all registered filters."""
        text = text.lower()

        for filter in self._filters:
            if not filter.is_clean(text):
                text = filter.censor(text, character=character)
        return ". ".join([sentence.strip().capitalize() for sentence in re.split("[.?!]", text)])
    
    
class EnglishCensorFilter(AbstractFilter):
    """English filter. Censor english swear words."""
    _words: list[str] = AbstractFilter._load_from_file("words/en.txt")

    def is_clean(text: str) -> bool:
        """Check if sentence contains swear words."""
        for word in EnglishCensorFilter._words:
            if re.search(word, text):
                return False
        return True
    
    def censor(text: str, character: str="*") -> str:
        """Censor swear words in sentence."""
        for word in EnglishCensorFilter._words:
            text = re.sub(word, character*len(word), text)
        return text  
    

class RussianCensorFilter(AbstractFilter):
    """Russian filter. Censor russian swear words."""
    _words: list[str] = AbstractFilter._load_from_file("words/ru.txt")

    def is_clean(text: str) -> bool:
        """Check if sentence contains swear words."""
        for word in RussianCensorFilter._words:
            if re.search(word, text):
                return False
        return True
    
    def censor(text: str, character: str="*") -> str:
        """Censor swear words in sentence."""
        for word in RussianCensorFilter._words:
            text = re.sub(word, character*len(word), text)
        return text 


class UkrainianCensorFilter(AbstractFilter):
    """Ukrainian filter. Censor ukrainian swear words."""
    _words: list[str] = AbstractFilter._load_from_file("words/ua.txt")

    def is_clean(text: str) -> bool:
        """Check if sentence contains swear words."""
        for word in UkrainianCensorFilter._words:
            if re.search(word, text):
                return False
        return True
    
    def censor(text: str, character: str="*") -> str:
        """Censor swear words in sentence."""
        for word in UkrainianCensorFilter._words:
            text = re.sub(word, character*len(word), text)
        return text 
