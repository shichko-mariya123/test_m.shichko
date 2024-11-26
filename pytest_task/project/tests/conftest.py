import pytest

from pytest_task.config import URL
from pytest_task.framework.utils.table_processor import TableProcessor
from pytest_task.project.tests.test_wikitables import TABLE_TYPE


@pytest.fixture
def table_processor():
    processor = TableProcessor(URL, TABLE_TYPE)
    processor.fetch_table()
    return processor
