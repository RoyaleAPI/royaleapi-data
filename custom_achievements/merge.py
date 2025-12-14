import pandas as pd

source_paths = [
    "clean_main.csv",
    "clean_2v2.csv",
    "clean_mt.csv",
    "clean_retro.csv",
]

out_path = "royaleapi_custom_achievements_items.csv"

column_types = {
    "ach_key": "string",
    "player_id": "Int64",
    "player_name": "string",
    "player_tag": "string",
    "value": "Int64",
    "value_str": "string",
    "value_2": "Int64",
    "is_visible": "Int64",
    "timestamp": "datetime64[ns]",
    "comment": "string",
    "link": "string",
    "royaleapi_path": "string",
}

pd_data = pd.DataFrame()
for file_path in source_paths:
    pd_data_part = pd.read_csv(file_path)
    pd_data = pd.concat([pd_data, pd_data_part])

pd_data = pd_data.astype(column_types)
pd_data.to_csv(out_path, index=False, header=True, date_format="%Y-%m-%d")
