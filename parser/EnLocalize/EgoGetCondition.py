from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_EGO_Get_Condition/EN_EGO_Get_Condition.json"


class Data(BaseModel):
    id: str
    content: str


class EgoGetCondition(BaseModel):
    dataList: List[Data]


def ego_get_condition():
    return EgoGetCondition.parse_file(FILE).dict()


def select_ego_get_condition_by_id(condition_id: str) -> Optional[Data]:
    all_data = ego_get_condition()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == condition_id:
            return Data(**data_entry)

    print(f"No ego get condition found with id {condition_id}")
    return None
