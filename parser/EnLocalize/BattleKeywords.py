from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_BattleKeywords/EN_BattleKeywords.json"


class Data(BaseModel):
    id: int
    name: str
    desc: str


class BattleKeywordsData(BaseModel):
    dataList: List[Data]


def battle_keywords():
    return BattleKeywordsData.parse_file(FILE).dict()


def select_battle_keywords_by_id(keyword_id: int) -> Optional[Data]:
    all_data = battle_keywords()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == keyword_id:
            return Data(**data_entry)

    print(f"No battle keyword found with id {keyword_id}")
    return None


def select_battle_keywords_by_name(keyword_name: str) -> Optional[Data]:
    all_data = battle_keywords()

    for data_entry in all_data["dataList"]:
        if data_entry["name"] == keyword_name:
            return Data(**data_entry)

    print(f"No battle keyword found with name {keyword_name}")
    return None
