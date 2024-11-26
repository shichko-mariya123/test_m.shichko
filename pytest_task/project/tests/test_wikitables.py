import pytest

from pytest_task.framework.constants.column_keywords import ColumnKeywords
from pytest_task.framework.utils.data_normalization import DataNormalization
from pytest_task.project.data_classes.website_data import WebsiteData

TABLE_TYPE = "wikitable"


class TestWebsitesData:
    @pytest.mark.parametrize("min_visitors",
                             [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_websites_popularity(self, min_visitors, table_processor):
        column_processor = {"popularity": DataNormalization.clean_numeric_column}
        data = table_processor.process_table(
            dataclass_type=WebsiteData,
            keywords=ColumnKeywords.WEBSITE_DATA,
            column_processors=column_processor,
        )

        failing_websites = [
            f"{site.websites} (Frontend:{site.frontend}|Backend:{site.backend}) has {site.popularity} unique visitors per month. "
            f"(Expected more than {int(min_visitors)})"
            for site in data if site.popularity < min_visitors
        ]

        assert not failing_websites, "\n".join(failing_websites)
