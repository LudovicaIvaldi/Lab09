from dataclasses import dataclass


@dataclass
class Volo:
    ID: int
    AIRLINE_ID: int
    FLIGHT_NUMBER: int
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    DISTANCE:int


    def __hash__(self):
        return hash((self.ID,self.AIRLINE_ID,self.ORIGIN_AIRPORT_ID, self.DESTINATION_AIRPORT_ID)) #chiave primaria

    def __eq__(self, other):
        return (self.ID == other.ID and
                self.AIRLINE_ID == other.AIRLINE_ID and
                self.ORIGIN_AIRPORT_ID==other.AORIGIN_AIRPORT_ID and
                self.DESTINATION_AIRPORT_ID==other.DESTINATION_AIRPORT_ID)



