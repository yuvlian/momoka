from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH


def skills_personality_file(x: str) -> str:
    return f"{BASE_PATH}EN_Skills_personality-{x}/EN_Skills_personality-{x}.json"


YI_SANG = skills_personality_file("01")
FAUST = skills_personality_file("02")
DON_QUIXOTE = skills_personality_file("03")
RYOSHU = skills_personality_file("04")
MEURSAULT = skills_personality_file("05")
HONG_LU = skills_personality_file("06")
HEATHCLIFF = skills_personality_file("07")
ISHMAEL = skills_personality_file("08")
RODION = skills_personality_file("09")
SINCLAIR = skills_personality_file("10")
OUTIS = skills_personality_file("11")
GREGOR = skills_personality_file("12")


class Desc(BaseModel):
    desc: Optional[str] = None


class Coin(BaseModel):
    coindescs: Optional[List[Desc]] = None


class Level(BaseModel):
    level: int
    name: str
    desc: str
    coinlist: List[Coin]


class Data(BaseModel):
    id: int
    levelList: List[Level]


class SkillsPersonalityData(BaseModel):
    dataList: List[Data]


def skills_yi_sang_data():
    return SkillsPersonalityData.parse_file(YI_SANG).dict()


def skills_faust_data():
    return SkillsPersonalityData.parse_file(FAUST).dict()


def skills_don_quixote_data():
    return SkillsPersonalityData.parse_file(DON_QUIXOTE).dict()


def skills_ryoshu_data():
    return SkillsPersonalityData.parse_file(RYOSHU).dict()


def skills_meursault_data():
    return SkillsPersonalityData.parse_file(MEURSAULT).dict()


def skills_hong_lu_data():
    return SkillsPersonalityData.parse_file(HONG_LU).dict()


def skills_heathcliff_data():
    return SkillsPersonalityData.parse_file(HEATHCLIFF).dict()


def skills_ishmael_data():
    return SkillsPersonalityData.parse_file(ISHMAEL).dict()


def skills_rodion_data():
    return SkillsPersonalityData.parse_file(RODION).dict()


def skills_sinclair_data():
    return SkillsPersonalityData.parse_file(SINCLAIR).dict()


def skills_outis_data():
    return SkillsPersonalityData.parse_file(OUTIS).dict()


def skills_gregor_data():
    return SkillsPersonalityData.parse_file(GREGOR).dict()


def all_skills_personality_data():
    return [
        skills_yi_sang_data(),
        skills_faust_data(),
        skills_don_quixote_data(),
        skills_ryoshu_data(),
        skills_meursault_data(),
        skills_hong_lu_data(),
        skills_heathcliff_data(),
        skills_ishmael_data(),
        skills_rodion_data(),
        skills_sinclair_data(),
        skills_outis_data(),
        skills_gregor_data(),
    ]


def select_skills_personality_by_id(
    personality_index: int, skill_id: int
) -> Optional[Data]:
    all_data = all_skills_personality_data()

    if personality_index < 0 or personality_index >= len(all_data):
        print(f"Invalid personality index: {personality_index}")
        return None

    personality_data = all_data[personality_index]

    for data_entry in personality_data["dataList"]:
        if data_entry["id"] == skill_id:
            return Data(**data_entry)

    print(
        f"No skill found with id {skill_id} for personality at index {personality_index}"
    )
    return None
