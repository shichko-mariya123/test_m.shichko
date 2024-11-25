from typing import cast, List

import pytest

from config import URL
from framework.utils.table_data_fetcher import clean_numeric_column, fetch_table_data, remove_square_brackets
from project.data_classes.website_data import WebsiteData



COLUMN_MAPPING = {
    "name": "websites",
    "frontend": "front-end (client-side)",
    "backend": "back-end (server-side)",
    "popularity": "popularity (unique visitors per month)[1]",
}

COLUMN_PROCESSORS = {
    "popularity": clean_numeric_column,
}


class TestProgrammingLanguagesPopularity:

    @pytest.mark.parametrize("min_visitors",
                             [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_unique_visitors_per_month(self, min_visitors):
        data = cast(List[WebsiteData], fetch_table_data(
            url=URL,
            table_class="wikitable",
            dataclass_type=WebsiteData,
            column_mapping=COLUMN_MAPPING,
            column_processors=COLUMN_PROCESSORS,
        ))

        failing_websites = [
            f"{site.name} (Frontend:{site.frontend}|Backend:{site.backend}) has {site.popularity} unique visitors per month. "
            f"(Expected more than {int(min_visitors)})"
            for site in data if site.popularity < min_visitors
        ]

        assert not failing_websites, "\n".join(failing_websites)
