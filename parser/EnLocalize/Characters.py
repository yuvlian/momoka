from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_Characters/EN_Characters.json"


class Data(BaseModel):
    id: int
    name: str


class CharactersData(BaseModel):
    dataList: List[Data]


def characters():
    return CharactersData.parse_file(FILE).dict()


def select_characters_by_id(character_id: int) -> Optional[Data]:
    all_data = characters()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == character_id:
            return Data(**data_entry)

    print(f"No character found with id {character_id}")
    return None


def select_characters_by_name(character_name: str) -> Optional[Data]:
    all_data = characters()

    for data_entry in all_data["dataList"]:
        if data_entry["name"] == character_name:
            return Data(**data_entry)

    print(f"No character found with name {character_name}")
    return None
