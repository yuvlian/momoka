from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_Personalities/EN_Personalities.json"


class Data(BaseModel):
    id: int
    title: str
    name: str
    nameWithTitle: str
    desc: str


class PersonalitiesData(BaseModel):
    dataList: List[Data]


def personalities():
    return PersonalitiesData.parse_file(FILE).dict()


def select_personality_by_id(personality_id: int) -> Optional[Data]:
    all_data = personalities()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == personality_id:
            return Data(**data_entry)

    print(f"No personality found with id {personality_id}")
    return None
