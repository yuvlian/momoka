from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_Passives/EN_Passives.json"


class Data(BaseModel):
    id: int
    name: str
    desc: str


class PassivesData(BaseModel):
    dataList: List[Data]


def passives():
    return PassivesData.parse_file(FILE).dict()


def select_passives_by_id(passive_id: int) -> Optional[Data]:
    all_data = passives()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == passive_id:
            return Data(**data_entry)

    print(f"No passive found with id {passive_id}")
    return None
