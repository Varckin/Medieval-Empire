from json import load, dump
from pathlib import Path


current_path: str = str(Path.cwd())


def read_json(file_name: str) -> dict:
    with open(file=f"{current_path}{file_name}", mode="r", encoding="utf-8") as read_file:
        return load(fp=read_file)
    

def write_json(file_name: str, dict_data: dict) -> None:
    with open(file=f"{current_path}{file_name}", mode="w", encoding="utf-8") as write_file:
        dump(obj=dict_data, fp=write_file, ensure_ascii=False, indent=4)

# Temporarily English
def getValue(key: str, lang: str = "EN") -> str:
    with open(file=f"{current_path}/Localization/{lang}.json", mode="w", encoding="utf-8") as file:
        localization: dict = load(fp=file)
        return localization.get(key)