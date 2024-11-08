from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from parser.EnLocalize import BASE_PATH

BASE_DIR = Path(BASE_PATH)
FILE_PATTERN = "EN_PanicInfo"


class Data(BaseModel):
    id: int
    panicName: str
    lowMoraleDescription: Optional[str] = None
    panicDescription: str


class PanicInfoData(BaseModel):
    dataList: List[Data]


def combine_panic_info_data() -> PanicInfoData:
    combined_data_list = []
    for file_path in BASE_DIR.rglob(f"{FILE_PATTERN}*.json"):
        print(f"Loading file: {file_path}")
        panic_info_data = PanicInfoData.parse_file(file_path)
        combined_data_list.extend(panic_info_data.dataList)
    return PanicInfoData(dataList=combined_data_list)


def panic_info() -> PanicInfoData:
    return combine_panic_info_data().dict()


def select_panic_info_by_panic_name(panic_name: str) -> Optional[Data]:
    all_data = panic_info()
    for data_entry in all_data.dataList:
        if data_entry.panicName == panic_name:
            return data_entry
    print(f"No panic info found with panicName {panic_name}")
    return None


def select_panic_info_by_id(panic_info_id: int) -> Optional[Data]:
    all_data = panic_info()
    for data_entry in all_data.dataList:
        if data_entry.id == panic_info_id:
            return data_entry
    print(f"No panic info found with id {panic_info_id}")
    return None
