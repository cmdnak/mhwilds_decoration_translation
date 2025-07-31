import pandas as pd
import json

# Load your JSON file
df = pd.read_json("json/fr_jewels.json")

# Create a new column by concatenating other fields
df["fr_concatenate"] = (
    df["name"] + " " +
    df["slot_lvl"].astype(str) + " " +
    df["talent_fr"] + " " +
    df["desc_merge"]
)

# Export the new DataFrame to JSON
with open("json/fr_jewels_with_concat.json", "w", encoding="utf-8") as f:
    json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=2)

print("✅ JSON concatenate ok")
