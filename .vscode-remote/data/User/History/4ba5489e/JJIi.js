// Initialize Flatpickr for the date field
flatpickr("#id_date", {
    dateFormat: "Y-m-d",
    minDate: "today",
});

// Initialize Flatpickr for the time field
flatpickr("#id_time", {
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",
    time_24hr: true,
});