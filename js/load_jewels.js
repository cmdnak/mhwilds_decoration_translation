// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
  fetch("../json/jewels_merged.json") // Adjust if needed
    .then(response => response.json())
    .then(data => {
      const tableBody = document.getElementById("jewel-table-body");
      tableBody.innerHTML = ""; // Clear any existing rows

      data.forEach(jewel => {
        const row = document.createElement("tr");

        // 🔸 Create each cell
        const nameCell = document.createElement("td");
        nameCell.textContent = jewel.name;

        const slotCell = document.createElement("td");
        slotCell.textContent = jewel.slot;

        const skillCell = document.createElement("td");
        skillCell.textContent = jewel.skill || "N/A";

        const descCell = document.createElement("td");
        descCell.textContent = jewel.description || "N/A";

        // 📥 Append all 4 cells to the row
        row.appendChild(nameCell);
        row.appendChild(slotCell);
        row.appendChild(skillCell);
        row.appendChild(descCell);

        // 📥 Append row to the table body
        tableBody.appendChild(row);
      });
    })
    .catch(error => {
      console.error("Failed to load jewel data:", error);
    });
});
