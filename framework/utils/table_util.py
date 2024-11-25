from dataclasses import is_dataclass, fields
from typing import List, Type, TypeVar

import pandas as pd
from pandas import DataFrame

from framework.utils.string_util import normalize_columns_names_from_wiki_table_for_test, preprocess

T = TypeVar("T")


def parse_tables(page_url: str) -> DataFrame:
    df = pd.read_html(page_url)[0]
    df = convert_numeric_columns(df)
    return df



def map_columns(df: pd.DataFrame, dataclass_fields: dict) -> dict:
    return {
        col: dataclass_fields[field]
        for col in df.columns
        for field in dataclass_fields
        if field in col or preprocess(field) in preprocess(col)
    }


def map_df_to_dataclass(df: pd.DataFrame, dataclass_type: Type[T]) -> List[T]:
    if not is_dataclass(dataclass_type):
        raise ValueError(f"{dataclass_type} must be a dataclass.")
    df = df.copy()
    df.columns = normalize_columns_names_from_wiki_table_for_test(df.columns)
    dataclass_fields = {field.name.lower(): field.name for field in fields(dataclass_type)}
    column_mapping = map_columns(df, dataclass_fields)
    if missing := set(dataclass_fields.values()) - set(column_mapping.values()):
        raise ValueError(f"Missing fields in the DataFrame: {missing}")
    return [dataclass_type(**{column_mapping[col]: row[col] for col in column_mapping}) for _, row in df.iterrows()]

def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col].str.replace(",", "").str.strip(), errors="coerce")
        except AttributeError:
            pass
    return df