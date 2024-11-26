from typing import Dict, Callable

import pandas as pd

from pytest_task.framework.utils.data_normalization import DataNormalization


class TableNormalizer:
    @staticmethod
    def normalize_columns(df: pd.DataFrame, column_mapping: Dict[str, str]) -> pd.DataFrame:
        df.columns = DataNormalization.normalize_column_names(df.columns)
        column_mapping = {k: v.lower() for k, v in column_mapping.items()}
        missing_columns = [v for v in column_mapping.values() if v not in df.columns]
        if missing_columns:
            raise ValueError(f"Expected columns not found: {missing_columns}")

        df.rename(columns={v: k for k, v in column_mapping.items()}, inplace=True)
        return df


    @staticmethod
    def process_columns(df: pd.DataFrame, column_processors: Dict[str, Callable[[pd.Series], pd.Series]]) -> pd.DataFrame:
        if column_processors:
            for col, processor in column_processors.items():
                if col in df.columns:
                    df[col] = processor(df[col])
        return df


    @staticmethod
    def remove_square_brackets(df: pd.DataFrame) -> pd.DataFrame:
        return df.applymap(
            lambda x: DataNormalization.remove_square_brackets(x) if isinstance(x, str) else x
        )