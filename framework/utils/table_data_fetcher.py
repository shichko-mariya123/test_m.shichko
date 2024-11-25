import re
from dataclasses import fields
from typing import Type, Dict, Callable, List

import pandas as pd
import requests
from bs4 import BeautifulSoup

from project.data_classes.table_row import TableRow


def normalize_column_names(columns):
    return [re.sub(r"\s+", " ", col).strip().lower() for col in columns]


def clean_numeric_column(column: pd.Series) -> pd.Series:
    return (
        column.astype(str)
        .str.replace(r"[^\d]", "", regex=True)
        .replace("", "0")
        .astype(int)
    )


def convert_row_to_dataclass(row, dataclass_type):
    dataclass_fields = {field.name for field in fields(dataclass_type)}
    row_dict = row.to_dict()
    filtered_row = {key: value for key, value in row_dict.items() if key in dataclass_fields}
    return dataclass_type(**filtered_row)


def fetch_table_data(
        url: str,
        table_class: str,
        dataclass_type: Type[TableRow],
        column_mapping: Dict[str, str],
        column_processors: Dict[str, Callable[[pd.Series], pd.Series]] = None,
) -> List[TableRow]:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': table_class})
    if not table:
        raise ValueError(f"Таблица с классом '{table_class}' не найдена.")

    df = pd.read_html(str(table))[0]

    df.columns = pd.Index([col.strip().lower().replace("\n", " ").replace("  ", " ") for col in df.columns])
    column_mapping = {k: v.lower() for k, v in column_mapping.items()}

    missing_columns = [v for v in column_mapping.values() if v not in df.columns]
    if missing_columns:
        raise ValueError(f"Expected columns are not found: {missing_columns}")

    df.rename(columns={v: k for k, v in column_mapping.items()}, inplace=True)

    if column_processors:
        for col, processor in column_processors.items():
            if col in df.columns:
                df[col] = processor(df[col])

    df = df.applymap(lambda x: remove_square_brackets(x) if isinstance(x, str) else x)

    data = [
        dataclass_type(**{field.name: row[field.name] for field in fields(dataclass_type) if field.name in row.index})
        for _, row in df.iterrows()
    ]

    return data


def find_matching_columns(df: pd.DataFrame, column_keywords: Dict[str, List[str]]) -> Dict[str, str]:
    matched_columns = {}
    for target, keywords in column_keywords.items():
        for col in df.columns:
            for keyword in keywords:
                if keyword in col.lower():
                    matched_columns[target] = col
                    break
            if target in matched_columns:
                break
        else:
            raise ValueError(f"Can not find column for '{target}' with keywords {keywords}.")
    return matched_columns


def remove_square_brackets(text: str) -> str:
    return re.sub(r"\[\d+]", "", text).strip()
