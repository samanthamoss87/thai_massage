const timepicker = new Timepicker('#timepicker', {
    format: 'HH:mm',
    minTime: '09:00',
    maxTime: '22:00',
    step: 30  // Step interval (e.g., 30 minutes)
});