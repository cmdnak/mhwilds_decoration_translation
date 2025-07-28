# ----------------------------------------
# 💻 Web Scraper for Game8 Monster Hunter Jewels
# Goal: Extract jewel name, slot, and skill
# Source: https://game8.co/games/Monster-Hunter-Wilds/archives/497352
# ----------------------------------------

# 1️⃣ Import required libraries
import requests                    # Used to download the webpage
from bs4 import BeautifulSoup      # Used to parse and extract HTML content
import json                        # Used to write structured data to disk

# 2️⃣ Define the target page URL
url = "https://game8.co/games/Monster-Hunter-Wilds/archives/497352"

# 3️⃣ Set a fake browser header so the site doesn’t block us
headers = {
    "User-Agent": "Mozilla/5.0"  # Pretend to be a regular user using a browser
}

# 4️⃣ Send a GET request to the website
response = requests.get(url, headers=headers)

# 5️⃣ Check if the page was downloaded successfully
if response.status_code == 200:
    print("✅ Page downloaded successfully!")
    html_data = response.text  # Save the HTML code as a string
else:
    print("❌ Failed to download page:", response.status_code)
    exit()  # Stop the program if we can’t download the page

# 6️⃣ Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_data, "html.parser")

# 7️⃣ Find the first <table> tag on the page (this is where the jewel data is)
table = soup.find("table", class_="a-table a-table table--fixed flexible-cell a-table")
if not table:
    print("❌ Specific jewel table not found — trying fallback.")
    tables = soup.find_all("table")
    print(f"🛠 Found {len(tables)} tables total.")
    for i, t in enumerate(tables):
        print(f"🔍 Table #{i} preview:")
        print(t.prettify()[:500])  # print the first 500 chars of each table
    exit()

# 8️⃣ Check if the table was actually found
if table:
    print("✅ Table found.")
else:
    print("❌ Table not found!")
    exit()

# 9️⃣ Find all the <tr> (table row) elements inside the table
rows = table.find_all("tr")
print(f"🔍 Number of rows found: {len(rows)}")  # Includes header row

# 🔎 Optional: Print the content of the first data row (skipping header)
if len(rows) > 1:
    print("🔎 First jewel row preview:")
    print(rows[1].prettify())
else:
    print("⚠️ Table has no data rows.")

# 🔟 Create an empty list to store extracted jewels
jewels = []

# 🔁 Loop over each table row
for row in rows:
    # Extract all <td> (table data) elements inside the row
    cells = row.find_all("td")

    # Continue only if there are at least 3 cells (name, slot, skill)
    if len(cells) >= 3:
        # --- Extract the jewel name from the first <td> ---
        name_cell = cells[0]  # Get the first column
        name_link = name_cell.find("a")  # Find the <a> link inside

        # 🧹 Normalize name: fix brackets and replace "Jwl" with "Jewel"
        if name_link:
            raw_name = name_link.get_text(strip=True)
            name = (
                raw_name
                .replace("【", " [")     # Replace Japanese brackets
                .replace("】", "]")
                .replace("Jwl", "Jewel")  # Correct spelling
            )
        else:
            name = "Unknown"

        # --- Extract the slot value from the second <td> ---
        slot = cells[1].get_text(strip=True)  # Clean text, e.g., "1"

        # --- Extract the skill name(s) from the third <td> ---
        skill_cell = cells[2]

        # Find all <div class="align"> blocks inside the skill cell
        skill_blocks = skill_cell.find_all("div", class_="align")

        skill_list = []  # will hold ["Horn Maestro Lv. 2", "Slugger Lv. 1"]

        # Loop through each block and extract skill name + level
        for block in skill_blocks:
            skill_name_tag = block.find("a")  # <a> tag inside each block
            level_text = (
                block.get_text(strip=True)
                .replace(skill_name_tag.get_text(strip=True), "")
                .strip()
                if skill_name_tag else ""
            )

            # Combine "SkillName Lv. X"
            if skill_name_tag:
                full_skill = f"{skill_name_tag.get_text(strip=True)} {level_text}"
                skill_list.append(full_skill)

        # Join with " & " if multiple skills, else use first
        skill = " & ".join(skill_list) if skill_list else "Unknown"

        # --- Store the data as a dictionary ---
        jewels.append({
            "name": name,
            "slot": slot,
            "skill": skill
        })

# 💾 Step 11 – Save extracted data to a local JSON file
output_path = "json/jewels.json"

# Open the file and write JSON data into it
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(jewels, f, ensure_ascii=False, indent=2)

print(f"✅ Saved {len(jewels)} jewels to {output_path}")
