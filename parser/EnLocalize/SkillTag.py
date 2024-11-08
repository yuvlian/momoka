from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_SkillTag/EN_SkillTag.json"


class Data(BaseModel):
    id: str
    name: str


class SkillTagData(BaseModel):
    dataList: List[Data]


def skill_tag():
    return SkillTagData.parse_file(FILE).dict()


def select_skill_tag_by_id(skill_id: str) -> Optional[Data]:
    skill_data = skill_tag()
    for item in skill_data["dataList"]:
        if item["id"] == skill_id:
            return item
    print(f"No skill found with id: {skill_id}")
    return None


def select_skill_tag_by_name(skill_name: str) -> Optional[Data]:
    skill_data = skill_tag()
    for item in skill_data["dataList"]:
        if item["name"] == skill_name:
            return item
    print(f"No skill found with name: {skill_name}")
    return None
