from dataclasses import dataclass


@dataclass
class Aeroporto:
    ID: int
    IATA_CODE: str
    AIRPORT:str

    def __hash__(self):
        return hash(self.ID) #chiave primaria

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return f"{self.AIRPORT} ({self.IATA_CODE})"
