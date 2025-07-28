// Wait for the full HTML document to load
document.addEventListener("DOMContentLoaded", () => {
  // Get reference to the input field
  const searchInput = document.getElementById("searchInput");

  // Get the reset button element
  const resetBtn = document.getElementById("resetBtn");

  // When user types in the input field
  searchInput.addEventListener("input", () => {
    const searchTerm = searchInput.value.toLowerCase();

    // ✅ Live query the rows each time the input changes
    const rows = document.querySelectorAll("tbody tr");

    rows.forEach(row => {
      const col1 = row.cells[0]?.textContent.toLowerCase() || ""; // Jewel Name
      const col3 = row.cells[2]?.textContent.toLowerCase() || ""; // Description

      // If either column includes the search term → show the row
      const match = col1.includes(searchTerm) || col3.includes(searchTerm);

      // Animate via class toggle instead of direct .style
      if (match) {
        row.style.display = "";     // Show row
      } else {
        row.style.display = "none"; // Hide row
      }
    });
  });

  // When the user clicks the "Reset" button
  resetBtn.addEventListener("click", () => {
    // Clear the input field
    searchInput.value = "";

    // ✅ Get all rows dynamically and show them
    const rows = document.querySelectorAll("tbody tr");
    rows.forEach(row => {
      row.style.display = ""; // Show all rows again
    });
  });

  // === NEW: Toggle table collapse animation ===

  // Get the toggle button and the table wrapper element
  const toggleBtn = document.getElementById("toggleTableBtn");
  const tableWrapper = document.querySelector(".table-wrapper"); // ✅ changed from <table> to wrapper

  // Track if the table is visible
  let tableVisible = true;

  // When the user clicks the toggle button
  toggleBtn.addEventListener("click", () => {
    tableVisible = !tableVisible; // flip the boolean (true → false, false → true)

    // ✅ Instead of display: none, use class toggle on wrapper for smooth animation
    if (tableVisible) {
      tableWrapper.classList.remove("table--collapsed");         // Remove collapsing class to expand
      toggleBtn.textContent = "Hide Table";                      // Update button label
    } else {
      tableWrapper.classList.add("table--collapsed");            // Add class to animate shrinking
      toggleBtn.textContent = "Show Table";                      // Update button label
    }
  });
});


// === Image reveal on hover (Top Bar Banner Animation) ===
document.addEventListener("DOMContentLoaded", () => {
  const topBar = document.querySelector(".top-bar");
  const image = document.querySelector(".top-bar-img");
  
  topBar.addEventListener("mousemove", (e) => {
    const rect = topBar.getBoundingClientRect();
    const cursorY = e.clientY - rect.top;
    const percent = (cursorY / rect.height) * 100;
    
    // Image slides from bottom to cursor position
    image.style.clipPath = `inset(${percent}% 0 0 0)`;
  });
  
  topBar.addEventListener("mouseleave", () => {
    // Hide image completely
    image.style.clipPath = "inset(100% 0 0 0)";
  });
});
