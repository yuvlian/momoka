from pydantic import BaseModel
from typing import List, Optional
from parser.EnLocalize import BASE_PATH

FILE = BASE_PATH + "EN_AttributeText/EN_AttributeText.json"


class Data(BaseModel):
    id: str
    name: str


class AttributeTextData(BaseModel):
    dataList: List[Data]


def attribute_text():
    return AttributeTextData.parse_file(FILE).dict()


def select_attribute_text_by_id(attribute_id: str) -> Optional[Data]:
    all_data = attribute_text()

    for data_entry in all_data["dataList"]:
        if data_entry["id"] == attribute_id:
            return Data(**data_entry)

    print(f"No attribute text found with id {attribute_id}")
    return None


def select_attribute_text_by_name(attribute_name: str) -> Optional[Data]:
    all_data = attribute_text()

    for data_entry in all_data["dataList"]:
        if data_entry["name"] == attribute_name:
            return Data(**data_entry)

    print(f"No attribute text found with name {attribute_name}")
    return None
