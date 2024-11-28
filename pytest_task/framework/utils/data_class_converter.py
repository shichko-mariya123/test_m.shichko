from dataclasses import fields
from typing import Type, List
import pandas as pd


class DataclassConverter:
    @staticmethod
    def convert(df: pd.DataFrame, dataclass_type: Type) -> List:
        return [
            dataclass_type(
                **{field.name: row[field.name] for field in fields(dataclass_type) if field.name in row.index}
            )
            for _, row in df.iterrows()
        ]
