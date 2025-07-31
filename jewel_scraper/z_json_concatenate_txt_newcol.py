import pandas as pd
import json

# Load the JSON data
df = pd.read_json("json/jewels_merged.json")

# 🔧 Force slot_lvl to be integer
df["slot"] = df["slot"].astype("Int64")  # Ensures no .0 when exporting

# 🧠 Create the concatenated field
df["en_concatenate"] = (
    df["name"] + " " +
    df["slot"].astype(str) + " " +  # Concatenate as string
    df["skill"] + " " +
    df["description"]
)

# Save the updated JSON
with open("json/jewels_merged.json", "w", encoding="utf-8") as f:
    json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=2)

print("✅ JSON concatenate ok")
