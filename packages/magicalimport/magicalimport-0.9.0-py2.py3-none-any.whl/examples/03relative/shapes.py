import dataclasses


@dataclasses.dataclass
class Config:
    host: str
    port: int = 55555
