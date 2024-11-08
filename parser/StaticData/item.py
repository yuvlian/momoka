from pydantic import BaseModel
from typing import List, Optional
from parser.StaticData import BASE_PATH
from pathlib import Path

FOLDER = BASE_PATH + "item"


class ItemFunctionData(BaseModel):
    itemUseFuncType: str
    itemUseFuncValue: Optional[int] = None
    itemUseFuncString: Optional[str] = None


class ItemUiConfigData(BaseModel):
    tags: List[str]


class ItemContentData(BaseModel):
    type: str
    id: int
    num: Optional[int] = None
    minNum: Optional[int] = None
    maxNum: Optional[int] = None


class ItemSeasonTargetElementData(BaseModel):
    type: str
    id: int


class Data(BaseModel):
    id: int
    ignoreExcess: Optional[bool] = None
    season: Optional[int] = None
    seasonalTargetElement: Optional[ItemSeasonTargetElementData] = None
    contentsOpenType: Optional[str] = None
    contents: Optional[List[ItemContentData]] = None
    category: Optional[str] = None
    itemUseType: Optional[str] = None
    spriteStr: Optional[str] = None
    optionalSample: Optional[ItemContentData] = None
    itemUseFuncs: Optional[List[ItemFunctionData]] = None
    uiConfig: Optional[ItemUiConfigData] = None


class ItemData(BaseModel):
    list: List[Data]


def parse_item_file(file_path: Path) -> Optional[ItemData]:
    try:
        return ItemData.parse_file(file_path)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None


def all_item() -> List[ItemData]:
    item_data_list = [
        item_data
        for file_path in Path(FOLDER).rglob("*.json")
        if (item_data := parse_item_file(file_path))
    ]
    return item_data_list


def select_item_by_id(item_id: int) -> Optional[Data]:
    target_file = f"item-{item_id}.json"
    for file_path in Path(FOLDER).rglob(target_file):
        if item_data_list := parse_item_file(file_path):
            for item in item_data_list.list:
                if item.id == item_id:
                    return item
    print(f"File {target_file} not found in {FOLDER}")
    return None
