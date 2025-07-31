import pandas as pd  # 📊 Read spreadsheet tables
import json           # 🔁 Convert Python data to JSON

# 1️⃣ Load the Excel file (replace with your file path)
excel_file = "joyaux_desc/fr_jewels.xlsx"

# 2️⃣ Load a specific sheet (optional if you only have one sheet)
df = pd.read_excel(excel_file, sheet_name="desc_only")  # or sheet_name="Sheet1"

# 3️⃣ Convert DataFrame to a list of dictionaries (one per row)
data = df.to_dict(orient="records")

# 4️⃣ Save to JSON file
output_path = "/Users/Kims/Desktop/Yahnis_test/project_joyaux/json/fr_jewels.json"
with open("fr_jewels.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ JSON file created successfully.")
