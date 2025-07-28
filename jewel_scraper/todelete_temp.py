import json
import pandas as pd

with open("json/jewels_merged.json", "r", encoding="utf-8") as f:
    data = json.load(f)

unique_pairs = set()
for item in data:
    name = item["name"]
    skill_desc = item["description"]
    unique_pairs.add((name, skill_desc))
    
df = pd.DataFrame(list(unique_pairs), columns=["Name", "Skill"])
df.to_excel('output.xlsx', index=False)

df = pd.DataFrame(list(unique_pairs), columns=["Name", "Skill"])
print(df)

