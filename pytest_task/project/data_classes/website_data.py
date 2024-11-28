from dataclasses import dataclass


@dataclass
class WebsiteData:
    websites: str
    popularity: int
    frontend: str
    backend: str
