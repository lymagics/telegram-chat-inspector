from abc import ABC, abstractstaticmethod

from better_profanity import profanity
from obscene_words_filter import get_default_filter


class AbstractFilter(ABC):
    """Abstract filter.
    
    you can inherit it to create your own logic.
    """
    @abstractstaticmethod
    def is_clean(text: str) -> bool:
        """Check if sentence contains swear words."""
        pass 
    
    @abstractstaticmethod
    def censor(text: str) -> str:
        """Censor swear words in sentence."""
        pass 
    
    
class EnglishCensorFilter(AbstractFilter):
    """English filter.
    
    filter english words.
    """
    _filter = profanity
    _filter.load_censor_words()
    
    @staticmethod
    def is_clean(text: str) -> bool:
        """Check if sentence contains swear words."""
        return not EnglishCensorFilter._filter.contains_profanity(text) 
    
    @staticmethod
    def censor(text: str) -> str:
        """Censor swear words in sentence."""
        return EnglishCensorFilter._filter.censor(text)
    
    
class RussianCensorFilter(AbstractFilter):
    """Russian filter.
    
    filter russian words.
    """
    _filter = get_default_filter()
    
    @staticmethod
    def is_clean(text: str) -> bool:
        """Check if sentence contains swear words."""
        return not bool([m.group() for m in RussianCensorFilter._filter.find_bad_word_matches(text)])
    
    @staticmethod
    def censor(text: str) -> str:
        """Censor swear words in sentence."""
        return RussianCensorFilter._filter.mask_bad_words(text)
    