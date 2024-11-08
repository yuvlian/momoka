from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from parser.EnLocalize import BASE_PATH

BASE_DIR = Path(BASE_PATH)
FILE_PATTERN = "EN_Announcer"


class Data(BaseModel):
    id: int
    name: str


class AnnouncerData(BaseModel):
    dataList: List[Data]


def combine_announcer_data() -> AnnouncerData:
    combined_data_list = []
    for file_path in BASE_DIR.rglob("EN_Announcer*.json"):
        if "BattleAnnouncerDlg" not in file_path.parts and file_path.parts[
            -2
        ].startswith("EN_Announcer"):
            print(f"Loading file: {file_path}")
            announcer_data = AnnouncerData.parse_file(file_path)
            combined_data_list.extend(announcer_data.dataList)
    return AnnouncerData(dataList=combined_data_list)


def announcer() -> dict:
    return combine_announcer_data().dict()


def select_announcer_by_id(announcer_id: int) -> Optional[Data]:
    all_data = announcer()
    for data_entry in all_data["dataList"]:
        if data_entry["id"] == announcer_id:
            return Data(**data_entry)
    print(f"No announcer found with id {announcer_id}")
    return None


def select_announcer_by_name(announcer_name: str) -> Optional[Data]:
    all_data = announcer()
    for data_entry in all_data["dataList"]:
        if data_entry["name"] == announcer_name:
            return Data(**data_entry)
    print(f"No announcer found with name {announcer_name}")
    return None


print(announcer())
