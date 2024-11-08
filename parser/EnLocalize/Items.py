from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from parser.EnLocalize import BASE_PATH

BASE_DIR = Path(BASE_PATH)
FILE_PATTERN = "EN_Items"


class Data(BaseModel):
    id: int
    name: str
    desc: str
    flavor: str


class ItemData(BaseModel):
    dataList: List[Data]


def combine_item_data() -> ItemData:
    combined_data_list = []
    for file_path in BASE_DIR.rglob("EN_Items*.json"):
        print(f"Loading file: {file_path}")
        item_data = ItemData.parse_file(file_path)
        combined_data_list.extend(item_data.dataList)
    return ItemData(dataList=combined_data_list)


def items() -> dict:
    return combine_item_data().dict()


def select_item_by_id(item_id: int) -> Optional[Data]:
    all_data = items()
    for data_entry in all_data["dataList"]:
        if data_entry["id"] == item_id:
            return Data(**data_entry)
    print(f"No item found with id {item_id}")
    return None


def select_item_by_name(item_name: str) -> Optional[Data]:
    all_data = items()
    for data_entry in all_data["dataList"]:
        if data_entry["name"] == item_name:
            return Data(**data_entry)
    print(f"No item found with name {item_name}")
    return None


print(items())
