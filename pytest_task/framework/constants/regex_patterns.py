import re


class RegexPatterns:
    REMOVE_EXTRA_SPACES = re.compile(r"\s+")
    EXTRACT_NUMBERS = re.compile(r"\D")
    REMOVE_SQUARE_BRACKETS = re.compile(r"\[\d+]")
