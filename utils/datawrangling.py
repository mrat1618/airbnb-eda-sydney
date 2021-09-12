import pandas as pd 
import ast

def create_amenities_list(amenities:set, data:str)->None:
    """Extract unique amenities from the dataset.

    Args:
        amenities (set): empty set to store amenities
        data (str): cell value: str(list[str])
    """
    values_to_add = set(ast.literal_eval(data))
    values_to_add = values_to_add - amenities
    amenities.update(values_to_add)
    

def update_amenities_dict(row:pd.Series, amenities_dict:dict)->None:
    rtype = row.room_type
    for amn in ast.literal_eval(row.amenities):
        amenities_dict[rtype][amn] += 1