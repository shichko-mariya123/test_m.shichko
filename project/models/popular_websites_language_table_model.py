from dataclasses import dataclass

@dataclass
class PopularWebsitesLanguagesTableModel:
    websites: str
    popularity: int
    frontend: str
    backend: str
    database: str
    notes: str
