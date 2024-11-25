from dataclasses import dataclass

from project.data_classes.table_row import TableRow


@dataclass
class WebsiteData(TableRow):
    name: str
    frontend: str
    backend: str
    popularity: int
