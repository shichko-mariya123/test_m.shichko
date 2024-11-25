from decimal import Decimal

import pytest

from config import URL
from framework.utils.table_util import *
from project.models.popular_websites_language_table_model import PopularWebsitesLanguagesTableModel


class TestProgrammingLanguagesPopularity:

    @pytest.mark.parametrize("min_visitors",
                             [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_unique_visitors_per_month(self, min_visitors):
        df = parse_tables(URL)
        data = map_df_to_dataclass(df, PopularWebsitesLanguagesTableModel)
        failing_websites = [
            f"{site.websites} (Frontend:{site.frontend}|Backend:{site.backend}) has {site.popularity} unique visitors per month. "
            f"(Expected more than {int(min_visitors)})"
            for site in data if site.popularity < min_visitors
        ]
        assert not failing_websites, "\n".join(failing_websites)
