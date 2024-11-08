from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from parser.EnLocalize import BASE_PATH

BASE_DIR = Path(BASE_PATH)
FILE_PATTERN = "BattleAnnouncerDlg"


class Data(BaseModel):
    id: str
    dlg: str


class BattleAnnouncerDlgData(BaseModel):
    dataList: List[Data]


def combine_battle_announcer_dlg_data() -> BattleAnnouncerDlgData:
    combined_data_list = []
    for file_path in BASE_DIR.rglob("BattleAnnouncerDlg/**/*.json"):
        if "BattleAnnouncerDlg" in file_path.parts:
            print(f"Loading file: {file_path}")
            battle_announcer_data = BattleAnnouncerDlgData.parse_file(file_path)
            combined_data_list.extend(battle_announcer_data.dataList)
    return BattleAnnouncerDlgData(dataList=combined_data_list)


def battle_announcer_dlg() -> dict:
    return combine_battle_announcer_dlg_data().dict()


def select_battle_announcer_dlg_by_id(dlg_id: str) -> Optional[Data]:
    all_data = battle_announcer_dlg()
    for data_entry in all_data["dataList"]:
        if data_entry["id"] == dlg_id:
            return Data(**data_entry)
    print(f"No battle announcer dialogue found with id {dlg_id}")
    return None
