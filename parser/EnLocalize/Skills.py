from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_Skills/EN_Skills.json"


class Desc(BaseModel):
    desc: Optional[str] = None


class Coin(BaseModel):
    coindescs: Optional[List[Desc]] = None


class Level(BaseModel):
    level: int
    name: str
    desc: str
    keywords: Optional[List[str]] = None
    coinlist: Optional[List[Coin]] = None


class Data(BaseModel):
    id: int
    levelList: List[Level]


class SkillsData(BaseModel):
    dataList: List[Data]


def skills():
    return SkillsData.parse_file(FILE).dict()


def select_skills_by_id(skill_id: int) -> Optional[Data]:
    all_data = skills()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == skill_id:
            return Data(**data_entry)

    print(f"No skill found with id {skill_id}")
    return None
