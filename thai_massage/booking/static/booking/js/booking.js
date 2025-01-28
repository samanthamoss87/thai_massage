const calendar = document.getElementById("calendar");
const currentMonth = document.getElementById("currentMonth");
const prevMonthBtn = document.getElementById("prevMonth");
const nextMonthBtn = document.getElementById("nextMonth");

let date = new Date();
let selectedDay = null;
const selectedClass = 'selected-btn';

function renderCalendar() {
  calendar.innerHTML = "";

  const month = date.getMonth();
  const year = date.getFullYear();
  currentMonth.textContent = date.toLocaleDateString("en-US", {
    month: "long",
    year: "numeric",
  });

  // Days of the week headers
  const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  daysOfWeek.forEach((day) => {
    const dayHeader = document.createElement("div");
    dayHeader.className = "day-header";
    dayHeader.textContent = day;
    calendar.appendChild(dayHeader);
  });

  // Get the first day of the month
  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();

  // Render empty cells for days before the first day of the month
  for (let i = 0; i < firstDay; i++) {
    const emptyCell = document.createElement("div");
    emptyCell.className = "day-cell-empty";
    calendar.appendChild(emptyCell);
  }

  // Render days
  for (let i = 1; i <= daysInMonth; i++) {
    const dayCell = document.createElement("div");
    dayCell.className = "day-cell";
    dayCell.textContent = i;

    // Add click event listener to each day cell
    dayCell.addEventListener("click", () => {
      if (selectedDay) {
        selectedDay.classList.remove(selectedClass);
      }
      dayCell.classList.add(selectedClass);
      selectedDay = dayCell;
      console.log(`You clicked on: ${i}`);
      alert(`Selected Date: ${i}`);
    });

    calendar.appendChild(dayCell);
  }
}

// Event listeners for navigation
prevMonthBtn.addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  selectedDay = null; // Clear selection on month change
  renderCalendar();
});

nextMonthBtn.addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  selectedDay = null; // Clear selection on month change
  renderCalendar();
});

// Initial render
renderCalendar();
