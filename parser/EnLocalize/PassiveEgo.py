from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from parser.EnLocalize import BASE_PATH

BASE_DIR = Path(BASE_PATH)

FILE_PATTERN = "EN_Passive_Ego"


class Data(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    desc: Optional[str] = None


class PassiveEgoData(BaseModel):
    dataList: List[Data]


def combine_passive_ego_data() -> PassiveEgoData:
    combined_data_list = []

    for file_path in BASE_DIR.rglob(f"{FILE_PATTERN}*.json"):
        print(f"Loading file: {file_path}")
        passive_ego_data = PassiveEgoData.parse_file(file_path)
        combined_data_list.extend(passive_ego_data.dataList)
    return PassiveEgoData(dataList=combined_data_list)


def passive_ego() -> PassiveEgoData:
    return combine_passive_ego_data().dict()


def select_passive_ego_by_id(passive_ego_id: int) -> Optional[Data]:
    all_data = passive_ego()

    for data_entry in all_data.dataList:
        if data_entry.id == passive_ego_id:
            return data_entry

    print(f"No passive ego found with id {passive_ego_id}")
    return None


print(passive_ego())
