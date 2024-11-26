from typing import Type, Dict, Callable, List

import pandas as pd

from pytest_task.framework.utils.column_mapper import ColumnMapper
from pytest_task.framework.utils.data_class_converter import DataclassConverter
from pytest_task.framework.utils.html_table_fetcher import HTMLTableFetcher
from pytest_task.framework.utils.table_normalizer import TableNormalizer


class TableProcessor:
    def __init__(self, url: str, table_class: str):
        self.fetcher = HTMLTableFetcher(url, table_class)
        self.normalizer = TableNormalizer()
        self.converter = DataclassConverter()
        self._df = None

    def fetch_table(self):
        self._df = self.fetcher.fetch()

    def process_table(
            self,
            dataclass_type: Type,
            keywords=str,
            column_processors: Dict[str, Callable[[pd.Series], pd.Series]] = None,
    ) -> List:
        if self._df is None:
            raise ValueError("Table not loaded. Call `fetch_table` first.")
        column_mapping = ColumnMapper.map_columns_by_keywords_to_fields(self._df, keywords)
        self._df = self.normalizer.normalize_columns(self._df, column_mapping)
        self._df = self.normalizer.process_columns(self._df, column_processors)
        self._df = self.normalizer.remove_square_brackets(self._df)

        return self.converter.convert(self._df, dataclass_type)
