# ----------------------------------------
# 🔁 Merge jewels.json with jewels_desc_from_excel.json
# Goal: Match by base name + slot to create a unified JSON
# ----------------------------------------

import json

# 📂 Paths to your JSON files
scraped_path = "json/jewels.json"
desc_path = "json/jewels_desc_from_excel.json"
output_path = "json/jewels_merged.json"

# 🧠 Helper to extract base name up to 'Jewel'
def extract_base_name(name: str) -> str:
    if "Jewel" in name:
        return name.split("Jewel")[0].strip() + " Jewel"
    return name.strip()

# 📥 Load both source files
with open(scraped_path, "r", encoding="utf-8") as f:
    scraped_data = json.load(f)

with open(desc_path, "r", encoding="utf-8") as f:
    desc_data = json.load(f)

# 🧠 Build a lookup: (base_name, slot_level) → description
desc_lookup = {}
for item in desc_data:
    base = extract_base_name(item["normalized_name"])
    slot = item.get("slot_level", 0)
    key = (base, slot)
    desc_lookup[key] = item["description"]

# 🔁 Merge each scraped jewel with its matching description
merged_data = []
for jewel in scraped_data:
    base = extract_base_name(jewel["name"])
    try:
        slot = int(jewel["slot"])
    except ValueError:
        slot = 0
    key = (base, slot)

    # Lookup the combined key
    description = desc_lookup.get(key, "N/A")
    jewel["description"] = description
    merged_data.append(jewel)

# 💾 Write the final merged output
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=2)

print(f"✅ Merged {len(merged_data)} jewels into: {output_path}")
