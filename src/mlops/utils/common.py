import os,yaml,joblib,json
from box.exceptions import BoxValueError
from src.mlops import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dictionaries(path_to_dict:list,verbose=True):
    for path in path_to_dict:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path:Path,data:dict):
    with open (path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f" json file saved at path {path}")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        content=json.load(f)
    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)

    