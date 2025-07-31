import pandas as pd
import json

# 1️⃣ Load the Excel file
excel_file = "joyaux_desc/fr_jewels.xlsx"

# 2️⃣ Load the sheet and force 'slot_lvl' as string
df = pd.read_excel(excel_file, sheet_name="fr", dtype={"slot_lvl": str})

# 2.5️⃣ Keep only selected columns
df = df[["name", "slot_lvl", "talent_fr", "desc_merge"]]

# 3️⃣ Convert to list of dictionaries
data = df.to_dict(orient="records")

# 4️⃣ Export to JSON
output_path = "/Users/Kims/Desktop/Yahnis_test/project_joyaux/json/fr_jewels.json"
with open("fr_jewels.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ JSON file created successfully.")
