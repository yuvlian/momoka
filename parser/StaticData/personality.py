from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from parser.StaticData import BASE_PATH

FOLDER = BASE_PATH + "personality"


class AttributeData(BaseModel):
    skillId: int
    number: int


class AtkResistData(BaseModel):
    type: str
    value: float


class PersonalityResistInfoData(BaseModel):
    atkResistList: List[AtkResistData]


class PersonalityBreakSectionData(BaseModel):
    sectionList: List[int]


class PersonalityMentalConditionID(BaseModel):
    conditionID: str


class PersonalityMentalConditionData(BaseModel):
    level: int
    conditionIDList: List[PersonalityMentalConditionID]


class PersonalityMentalConditionInfoData(BaseModel):
    add: List[PersonalityMentalConditionData]
    min: List[PersonalityMentalConditionData]


class PersonalityHpData(BaseModel):
    defaultStat: int
    incrementByLevel: float


class Data(BaseModel):
    id: int
    appearance: str
    unitKeywordList: List[str]
    associationList: List[str]
    characterId: int
    panicType: int
    season: Optional[int] = None
    defenseSkillIDList: List[int]
    panicSkillOnErosion: int
    slotWeightConditionList: List[str]
    rank: int
    hp: PersonalityHpData
    defCorrection: int
    minSpeedList: List[int]
    maxSpeedList: List[int]
    uniqueAttribute: str
    mentalConditionInfo: PersonalityMentalConditionInfoData
    breakSection: PersonalityBreakSectionData
    resistInfo: PersonalityResistInfoData
    attributeList: List[AttributeData]


class PersonalityData(BaseModel):
    list: List[Data]


def parse_personality_file(file_path: Path) -> Optional[PersonalityData]:
    try:
        return PersonalityData.parse_file(file_path)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None


def all_personality() -> List[PersonalityData]:
    personality_data_list = [
        personality_data
        for file_path in Path(FOLDER).rglob("*.json")
        if (personality_data := parse_personality_file(file_path))
    ]
    return personality_data_list


def select_personality_by_id(personality_id: int) -> Optional[PersonalityData]:
    target_file = f"personality-{personality_id}.json"
    for file_path in Path(FOLDER).rglob(target_file):
        if personality_data := parse_personality_file(file_path):
            return personality_data
    print(f"File {target_file} not found in {FOLDER}")
    return None
