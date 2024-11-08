from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from parser.StaticData import BASE_PATH

FOLDER = BASE_PATH + "ego"


class EgoCorrosionChanceData(BaseModel):
    section: float
    probability: float


class EgoRequirementData(BaseModel):
    attributeType: str
    num: int


class EgoAttributeResistData(BaseModel):
    type: str
    value: float


class Data(BaseModel):
    id: int
    characterId: int
    egoType: str
    egoClass: Optional[int] = None
    season: int
    skillTier: Optional[int] = None
    attributeResistList: List[EgoAttributeResistData]
    requirementList: List[EgoRequirementData]
    corrosionSectionList: List[EgoCorrosionChanceData]
    passiveList: Optional[List[None]] = None
    awakeningPassiveList: List[int]
    awakeningSkillId: int
    corrosionSkillId: Optional[int] = None


class EgoData(BaseModel):
    list: List[Data]


def parse_ego_file(file_path: Path) -> Optional[EgoData]:
    try:
        return EgoData.parse_file(file_path)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None


def all_ego() -> List[EgoData]:
    ego_data_list = [
        ego_data
        for file_path in Path(FOLDER).rglob("*.json")
        if (ego_data := parse_ego_file(file_path))
    ]
    return ego_data_list


def select_ego_by_id(ego_id: int) -> Optional[EgoData]:
    target_file = f"ego-{ego_id}.json"
    for file_path in Path(FOLDER).rglob(target_file):
        if ego_data := parse_ego_file(file_path):
            return ego_data
    print(f"File {target_file} not found in {FOLDER}")
    return None
