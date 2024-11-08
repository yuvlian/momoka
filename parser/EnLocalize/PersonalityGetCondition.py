from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_Personality_Get_Condition/EN_Personality_Get_Condition.json"


class Data(BaseModel):
    id: str
    content: str


class PersonalityGetCondition(BaseModel):
    dataList: List[Data]


def personality_get_condition():
    return PersonalityGetCondition.parse_file(FILE).dict()


def select_personality_get_condition_by_id(condition_id: str) -> Optional[Data]:
    all_data = personality_get_condition()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == condition_id:
            return Data(**data_entry)

    print(f"No condition found with id {condition_id}")
    return None
