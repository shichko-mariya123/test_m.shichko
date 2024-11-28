import requests
from bs4 import BeautifulSoup
import pandas as pd


class HTMLTableFetcher:
    def __init__(self, url: str, table_class: str):
        self.url = url
        self.table_class = table_class


    def fetch(self) -> pd.DataFrame:
        response = requests.get(self.url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"class": self.table_class})
        if not table:
            raise ValueError(f"Table with class '{self.table_class}' not found.")

        return pd.read_html(str(table))[0]