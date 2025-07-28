# ----------------------------------------
# 📤 Export Excel Data to JSON for Jewel Info
# Goal: Normalize names, merge description fields, and extract slot level
# ----------------------------------------

import pandas as pd   # Used to read Excel files into a DataFrame
import json           # Used to export the data into JSON format

# 🔧 1. Set your input and output file paths
excel_path = "joyaux_desc/jewel_desc.xlsx"                 # <- Path to your Excel file
output_path = "json/jewels_desc_from_excel.json"           # <- Path to save the generated JSON

# 🔃 2. Define a helper function to normalize names
# This makes Excel-compatible names match the scraped JSON ones by replacing brackets
def normalize_name(name) -> str:
    if not isinstance(name, str):  # Catch missing or non-string values (e.g. NaN → float)
        return ""
    return name.replace("【", "[").replace("】", "]").strip()

# 📥 3. Load the Excel file using pandas
try:
    df = pd.read_excel(excel_path)
    print(f"✅ Excel loaded. {len(df)} rows found.")
except FileNotFoundError:
    print(f"❌ File not found: {excel_path}")
    exit()

# 🧹 4. Remove rows where 'Decoration Name' is missing to prevent matching errors
before = len(df)
df = df[df["Decoration Name"].notna()]
after = len(df)
print(f"🧹 Skipped {before - after} rows with missing 'Decoration Name'.")

# 🧹 5. Normalize jewel names for matching with scraped JSON later
df["normalized_name"] = df["Decoration Name"].apply(normalize_name)

# 🧠 6. Combine 'Description 1' and 'Description 2' into a single 'description' field
def combine_descriptions(row):
    desc1 = row.get("Description 1", "")
    desc2 = row.get("Description 2", "")
    desc1 = desc1.strip() if isinstance(desc1, str) else ""
    desc2 = desc2.strip() if isinstance(desc2, str) else ""
    if desc1 and desc2:
        return f"{desc1} & {desc2}"
    return desc1 or desc2 or "N/A"

df["description"] = df.apply(combine_descriptions, axis=1)

# 🧠 7. Extract slot level from the "Decoration Name"
def extract_slot_level(name: str) -> int:
    import re
    match = re.search(r"\[(\d+)\]", name)
    return int(match.group(1)) if match else 0  # Default to 0 if not found

df["slot_level"] = df["Decoration Name"].apply(extract_slot_level)

# 🗂 8. Choose only the columns we want to export into JSON
export_columns = ["normalized_name", "slot_level", "description"]
export_data = df[export_columns].to_dict(orient="records")

# 💾 9. Write the cleaned and transformed data to JSON
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(export_data, f, ensure_ascii=False, indent=2)

print(f"✅ Excel data exported to {output_path}")
