from framework.constants.normalization_patterns import *


def normalize_columns_names_from_wiki_table_for_test(columns):
    return columns.str.strip().str.lower().str.replace(SPACE_PATTERN, UNDERSCORE).str.replace(SPACE_PATTERN,
                                                                                              EMPTY_STRING, regex=True)


def preprocess(text: str) -> str:
    return ''.join(char for char in text.lower() if char.isalpha())