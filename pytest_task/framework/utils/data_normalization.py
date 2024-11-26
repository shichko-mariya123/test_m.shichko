from typing import List

import pandas as pd

from pytest_task.framework.constants.regex_patterns import RegexPatterns
from pytest_task.framework.constants.string_constants import Strings


class DataNormalization:
    @staticmethod
    def normalize_text(text: str) -> str:
        return RegexPatterns.REMOVE_EXTRA_SPACES.sub(Strings.SPACE, text).strip().lower()

    @staticmethod
    def extract_numbers(text: str) -> str:
        if not isinstance(text, str):
            return Strings.EMPTY
        return RegexPatterns.EXTRACT_NUMBERS.sub(Strings.EMPTY, text)

    @staticmethod
    def remove_square_brackets(text: str) -> str:
        return RegexPatterns.REMOVE_SQUARE_BRACKETS.sub(Strings.EMPTY, text).strip()

    @staticmethod
    def clean_numeric_column(column: pd.Series) -> pd.Series:
        return column.astype(str).apply(DataNormalization.extract_numbers).replace(Strings.EMPTY,
                                                                                   Strings.DEFAULT_NUMBER).astype(int)

    @staticmethod
    def normalize_column_names(columns: List[str]) -> List[str]:
        return [DataNormalization.normalize_text(col) for col in columns]
