from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_Egos/EN_Egos.json"


class Data(BaseModel):
    id: int
    name: str
    desc: str


class EgosData(BaseModel):
    dataList: List[Data]


def egos():
    return EgosData.parse_file(FILE).dict()


def select_egos_by_id(ego_id: int) -> Optional[Data]:
    all_data = egos()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == ego_id:
            return Data(**data_entry)

    print(f"No ego found with id {ego_id}")
    return None
